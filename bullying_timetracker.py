import argparse
import time

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description='ArgParser')
	parser.add_argument('--hourly-rate', type=float, help='what you get paid in dollars per hour')
	parser.add_argument('--annual-salary', type=float, help='what you get paid per year')
	args = parser.parse_args()



	hourly_rate = (135e3/52)/40
	cost_incurred = 0
	prev_cost = 0
	start_time = time.time()
	print("Starting New Task")
	print("Whatever you're doing right now has cost...")
	try:
		while(True):
			time_elapsed = time.time() - start_time
			cost_incurred = ((hourly_rate / 60) / 60) * time_elapsed 

			
			if(int( (cost_incurred-prev_cost) * 100) >= 1):
				print("$", round(cost_incurred, 2))
				prev_cost = cost_incurred
			# time.sleep(1)
	except KeyboardInterrupt:
		pass
