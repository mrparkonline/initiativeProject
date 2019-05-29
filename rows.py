player_row = '''
<li class='list-group-item'>
<form><div class='form-row'>
	<div class='col-sm-2'>
		<input type="text" class="form-control" placeholder="Initiative">
	</div>
	<div class='col-sm-8'>
		<input type="text" class="form-control" placeholder="Player Name">
	</div>
	<div class='col-sm-2'>
		<button type='button' class='btn btn-outline-secondary'>D</button>
		<button type='button' class='btn btn-outline-danger'>X</button>
	</div>
</div></form>
</li>
'''

def Rows():
	rows = []

	return rows
# end of Rows

def addRow(arg):
	temp_dict = {}
	a = list(arg.keys())
	print(a)

	if a[0] == 'player_btn':
		temp_dict = {'rowData': player_row}

	return temp_dict
