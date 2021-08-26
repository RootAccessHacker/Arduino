import serial


class IO:
	def __init__(self):
		# List with Operating Systems with which this program is compatible
		self.platforms = ['win32', 'linux', 'darwin']

	def execute(self):
		from sys import platform

		if self.platforms[0] in platform:
			return self.win_serial_ports()
		elif self.platforms[1] in platform:
			return self.linux_serial_ports()
		elif self.platforms[2] in platform:
			return self.mac_os_serial_ports()
		else:
			try:
				raise EnvironmentError('Unsupported platform')
			except EnvironmentError:
				print("Platform Not Supported.")
				exit(0)

	def win_serial_ports(self):
		from serial.tools import list_ports_windows

		open_ports = list_ports_windows.comports()
		output_dict = {}
		if open_ports.__len__() > 0:
			for port in open_ports:
				output_dict[f"poort{open_ports.index(port)}"] = port[0]
			return output_dict
		else:
			print("\nNo connected devices were found.\n")
			return {"WARNING": "NO DEVICES FOUND"}

	def linux_serial_ports(self):
		from serial.tools import list_ports

		ports = list_ports.comports()
		output = dict()

		if ports.__len__() > 0:
			for port in ports:
				output[f"poort{ports.index(port)}"] = port[0]
			return output
		else:
			print("\nNo connected devices were found.\n")
			return {"WARNING": "NO DEVICES FOUND"}

	def mac_os_serial_ports(self):
		from glob import glob
		# port = /dev/tty.*

		ports = glob('/dev/tty.*')
		result = dict()

		for i in range(len(ports)):
			try:
				s = serial.Serial(ports[i])
				s.close()
				result[f"poort{ports.index(ports[i])}"] = ports[i]
			except serial.SerialException:
				# print("Something went wrong")
				pass
		return result if len(result) > 0 else {"WARNING": "NO DEVICES FOUND"}


if __name__ == '__main__':
	port_searcher = IO()
	print(port_searcher.execute(), '\n')
