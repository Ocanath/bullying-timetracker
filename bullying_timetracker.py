import argparse
import time

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description='ArgParser')
	parser.add_argument('--hourly_rate', type=float, default=0, help='what you get paid in dollars per hour')
	parser.add_argument('--annual_salary', type=float, default=0, help='what you get paid per year')
	parser.add_argument('--dollar_increment', type=float, default=0.01, help="Amount in dollars to increment on the display")
	parser.add_argument('--sleep',type=float, default=0, help="time to sleep per loop iteration. Can interfere with proper display rate update")
	args = parser.parse_args()

	if(args.hourly_rate == 0 and args.annual_salary == 0):
		print("Error, please provide a salary")
		exit()

	if(args.hourly_rate != 0):
		hourly_rate = args.hourly_rate
	elif(args.annual_salary != 0):
		hourly_rate = (args.annual_salary/52/40)
		print("Using", hourly_rate, "as hourly rate")

	cost_incurred = 0
	prev_cost = 0
	start_time = time.time()
	print("Starting New Task")
	print("Whatever you're doing right now has cost...")
	try:
		while(True):
			time_elapsed = time.time() - start_time
			cost_incurred = ((hourly_rate / 60) / 60) * time_elapsed 

			
			if(int( (cost_incurred-prev_cost) / args.dollar_increment ) >= 1):
				print("$", round(cost_incurred, 2))
				prev_cost = cost_incurred

			if(args.sleep != 0):
				time.sleep(args.sleep)
   
	except KeyboardInterrupt:
		pass
