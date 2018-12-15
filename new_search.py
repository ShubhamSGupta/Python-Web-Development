def nsearch4letters(phrase:str , letter:str = 'aeiou') -> list :
	content = []
	found={}
	for l in phrase :
		if l in letter :
			found.setdefault(l, 0)
			found[l] += 1
	for k,v in sorted(found.items()):
		content.append([])
		item = str(k)+' was found '+str(v)+' time(s).'
		content[-1] = str(item)
	return content