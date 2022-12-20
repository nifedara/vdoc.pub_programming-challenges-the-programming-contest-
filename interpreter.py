#program counter
global pc
pc = 0

def pyInterpreter(filepath):

    #a list representing RAM
    ram = []
    for i in range(1000):
        ram.append('0000')

    #10 registers containing '0000'
    reg = []
    for i in range(10):
        reg.append('0000')
    print(reg)    

    #read file to ram
    def read_to_ram():
        with open(filepath, 'r') as text:
            file_lines = text.readlines()

            file_length = len(file_lines)

            if file_length > len(ram):
                    print('insufficient memory')
            else:
                for i in range(file_length):
                    ram[i] = file_lines[i].replace("\n", "")
    read_to_ram()

    print(ram)

    def set_register(d,n):
        reg[int(d)] = '000' + n

    def add_to_register(d,n):
        add = (int(reg[int(d)]) + int(n)) % 10000
        result = '000' + str(add)
        reg[int(d)] = result[-4:]

    def multiply_register_by_value(d,n):
        multiply = (int(reg[int(d)]) * int(n)) % 10000
        result = '000' + str(multiply)
        reg[int(d)] = result[-4:]

    def copy_register(d,s):
        reg[int(d)] = reg[int(s)]

    def sum_registers(d,s):
        sum =  (int(reg[int(d)]) + int(reg[int(s)])) % 10000
        result = '000' + str(sum)
        reg[int(d)] = result[-4:]

    def multiply_registers(d,s):
        m_registers =  (int(reg[int(d)]) * int(reg[int(s)])) % 10000
        result = '000' + str(m_registers)
        reg[int(d)] = result[-4:]

    def copy_ram_to_register(d,a):
        reg[int(d)] = ram[int(reg[int(a)])]

    def set_ram(s,a):
        ram[reg[int(a)]] = reg[int(s)]
    
    def subtract_value_from_reg(d,n):
        sub =  (int(reg[int(d)]) - int(n)) % 10000
        result = '000' + str(sub)
        reg[int(d)] = result[-4:]

    def subtract_regs(d,s):
        sub_reg =  (int(reg[int(d)]) - int(reg[int(s)])) % 10000
        result = '000' + str(sub_reg)
        reg[int(d)] = result[-4:]

    #execute instruction
    def execute_instruction():
        global pc
        instruction = ram[pc]
        
        if (instruction.startswith('10')):
            print(reg)
            quit()

        elif (instruction.startswith('02')):
            set_register(instruction[2], instruction[3])

        elif (instruction.startswith('03')):
            add_to_register(instruction[2], instruction[3])

        elif (instruction.startswith('04')):
            multiply_register_by_value(instruction[2], instruction[3])

        elif (instruction.startswith('05')):
            copy_register(instruction[2], instruction[3])

        elif (instruction.startswith('06')):
            sum_registers(instruction[2], instruction[3])

        elif (instruction.startswith('07')):
            multiply_registers(instruction[2], instruction[3])

        elif (instruction.startswith('08')):
            copy_ram_to_register(instruction[2], instruction[3])

        elif (instruction.startswith('09')):
            set_ram(instruction[2], instruction[3])

        elif (instruction.startswith('00')):
            if (int(reg[int(instruction[3])]) != 0):
                pc = int(reg[int(instruction[2])])-1

        elif (instruction.startswith('13')):
            subtract_value_from_reg(instruction[2], instruction[3])

        elif (instruction.startswith('16')):
            subtract_regs(instruction[2], instruction[3])

    global pc
    while pc < (len(ram)):
        execute_instruction()
        pc += 1       

pyInterpreter(r"C:\Users\host\Documents\interpreter -py\input.txt")

