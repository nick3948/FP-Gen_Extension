import sys

n = int(sys.argv[1])

with open('template_header.c', 'r', encoding='utf-8') as input:
    header = input.read()

with open('template_body.c', 'r', encoding='utf-8') as input:
    body = input.read()

# Generate metrinome program
# Each variation will be written to the same file for ease of use with Metrinome REPL
with open('sumfor.c', 'w', encoding='utf-8') as output:
    output.write(header)
    # 
    block = ''
    for i in range(n):
        block += '\tfor (int k=0; k<2; k++)\n'
        new_body = 'int sumfor' + str(i+1) + '()'
        new_body += body.replace('// REPLACE\n', block)
        output.write(new_body)