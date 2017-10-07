# Ok so pretend you're eventbrite. You have a list of (host_id, event_id) pairs. 
# You can show only 10 results per page, and you don't want to show two events with the same host on the same page. 
# Write a program that allocates events to pages and returns the list of events for each page
def eventbrite(events):
	page_number = 1
	pages_dict = {1:[]}
	host_dict = {}
	if len(events) == 0:
		return None
	for ev in events:
		page_found = False
		host_id = ev[0]
		event_id = ev[1]
		if host_id in host_dict:
			unusable_pages = host_dict[host_id]
		else:
			unusable_pages = []
		for page in pages_dict:
			if page not in unusable_pages:
				if len(pages_dict[page]) < 3:
					if host_id in host_dict:
						host_dict[host_id].append(page)
					else:
						host_dict[host_id] = [page]
					pages_dict[page].append((host_id, event_id))
					page_found = True
		if not page_found:
			page_number += 1
			pages_dict[page_number] = [(host_id, event_id)]
			if host_id in host_dict: 
				host_dict[host_id].append(page_number)
			else:
				host_dict[host_id] = [page_number]
	return pages_dict

#test cases:
print eventbrite([("A", 123), ("A", 123), ("B", 57), ("C", 75), ("D", 78), ("B", 90)])

#start 12:25
#use a dictionary to keep track of hosts and their pages, 
#if not enough pages, make a new page	

#search through pages O(#pages)
#search through hosts O(#hosts)
# class Event:
# 	def __init__(self, host_id, event_id):
# 		self.host = host_id
# 		self.event = event_id
# 		self.pages = [] 

# class Page:
# 	def __init__(self, page_number):
# 		self.events = []
# 		self.number = page_number
# 		self.len = len(self.events)

# 	def make_new_page(self):
# 		self.number = page_number + 1

# 	def return_events(self):
# 		return self.events

# #page = 10, so after len of list = 10, make a new page
# #check in dictionary, with host as key, if his 


