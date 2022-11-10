from pymodbus.register_read_message import ReadHoldingRegistersResponse
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method='rtu', port="COM2", baudrate=115200,  timeout=0.1)
connection = client.connect()

i = 1
read_vals = client.read_holding_registers(0, 1, unit=i)

while type(read_vals) != ReadHoldingRegistersResponse:
    print(i)
    read_vals = client.read_holding_registers(0, 1, unit=i)
    i += 1
