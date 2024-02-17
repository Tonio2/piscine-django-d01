import sys

def generate_empty_cell():
	html = '<td class="empty"></td>'
	return html

def generate_cell(data):
    html = '<td class="cell"><h4>' + data[0] + '</h4><ul><li>' + data[2] + '</li><li>' + data[3] + '</li><li>' + data[4] + '</li><li>' + data[5] + '</li></ul></td>'
    return html

def main():
	first_line = True
	html = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Periodic Table</title><link rel="stylesheet" type="text/css" href="style.css"></head><body><table class="periodic">'
	last_data = None
	data = [None, None, None, None, None, None]
	with open('periodic_table.txt', 'r') as f:
		for line in f:
			tmp = line.split("=")
			data[0] = tmp[0].strip()
			tmp2 = tmp[1].split(",")
			data[1] = tmp2[0].strip().split(":")[1].strip()
			data[2] = tmp2[1].strip().split(":")[1].strip()
			data[3] = tmp2[2].strip().split(":")[1].strip()
			data[4] = tmp2[3].strip().split(":")[1].strip()
			data[5] = tmp2[4].strip().split(":")[1].strip()
			if int(data[1]) == 0:
				html += '</tr><tr class="periodic-row">' if first_line == False else '<tr class="periodic-row">'
				last_data = None
			# import pdb; pdb.set_trace()
			if last_data != None and int(data[1]) - int(last_data) > 1:
				for i in range(int(last_data) + 1, int(data[1])):
					html += generate_empty_cell()
			html += generate_cell(data)
			last_data = data[1]
	html += '</tr></table></body></html>'
	with open('periodic_table.html', 'w') as f:
		f.write(html)
  
if __name__ == '__main__':
    main()