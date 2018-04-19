import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def evalMods(mods):
	t = 0
	zero_vect = []

	for v in mods:
		if v == 1:
			t += 1
		zero_vect.append(0)
	if t >= len(mods)-1:
		print("zero_vect was set")
		return zero_vect
	else:
		return mods

def findValue(vals,mods,index, priority="lower"):
	#mods = evalMods(mods)
	if priority == "lower":
			for lamb, v in enumerate(vals):
				if v == index -1 and mods[lamb] == 0:
					vals[lamb] +=1
					mods[lamb] +=1
					return True

	elif priority == "higher":
			for lamb, v in enumerate(vals):
				if v == index +1 and mods[lamb] == 0:
					vals[lamb] -=1
					mods[lamb] +=1
					return True
	else:
		return False

def main():
	vals = [1,1,2,3,3,5,5,3,7]
	mods = [0,0,0,0,0,0,0,0,0]
	modmax = 0
	#print("valCount: ", valCount(vals))
	print(vals)
	print(mods)
	print(valCount(vals))
	m1 = {}
	m2 = {}
	topdown=True
	while 0 not in valCount(vals) and len(vals) != len(set(vals)):
		print("in while statement")

		if valCount(vals)[len(vals)] == 0 and len(vals) == len(set(vals))+1:
			print("topdown set to false")
			topdown = False
		elif valCount(vals)[1] == 0 and len(vals) == len(set(vals))+1:
			print("topdown set to true")
			topdown = True

		for index, value in valCount(vals).items():
			print("looping on " + str(index) + " of loop through valCount with val: " + str(value))
			print("vals: ", vals)
			print("mods: ", mods)
			mod = evalMods(mods)

			if value == 0 and index-1 > 0 and index+1 <= len(vals) and topdown:

				if valCount(vals)[index-1] > valCount(vals)[index+1]:
					findValue(vals,mods,index, priority ="lower")
					break
				elif valCount(vals)[index-1] < valCount(vals)[index+1]:
					findValue(vals,mods,index, priority ="higher")
					break
				elif valCount(vals)[index-1] == valCount(vals)[index+1] and valCount(vals)[index-1] > 1:
					findValue(vals,mods,index, priority ="lower")
					break
				elif valCount(vals)[index-1] == valCount(vals)[index+1] and valCount(vals)[index-1] == 1:
					findValue(vals,mods,index, priority ="lower")
					break

			elif value == 0 and index-1 > 0 and index+1 <= len(vals) and topdown == False:
				if valCount(vals)[index-1] == valCount(vals)[index+1] and valCount(vals)[index-1] == 1:
					findValue(vals,mods,index, priority ="lower")
					break
				elif valCount(vals)[index-1] > valCount(vals)[index+1] and valCount(vals)[index+1]:
					findValue(vals,mods,index, priority ="lower")
					break
				elif valCount(vals)[index-1] < valCount(vals)[index+1]:
					findValue(vals,mods,index, priority ="higher")
					break
				elif valCount(vals)[index-1] == valCount(vals)[index+1] and valCount(vals)[index-1] > 1:
					findValue(vals,mods,index, priority ="higher")
					break

			elif value == 1 and index-1 > 0 and index+1 <= len(vals) and topdown:
				if valCount(vals)[index-1] > valCount(vals)[index+1]:
					findValue(vals,mods,index, priority ="lower")
					break
				elif valCount(vals)[index-1]<valCount(vals)[index+1]:
					findValue(vals,mods,index, priority ="higher")
					break
				elif valCount(vals)[index-1] == valCount(vals)[index+1] and valCount(vals)[index-1] == 1 :
					print("VALUE IS 1")
					findValue(vals,mods,index, priority ="higher")
					break

			elif index+1 > len(vals) and value == 0:
				findValue(vals,mods,index, priority ="lower")
				break
			elif index-1 <= 0 and value == 0 and topdown:
				findValue(vals,mods,index, priority ="higher")
				break

		print("\n-",valCount(vals), ":", topdown)
		print("\t", vals)
		print("\t", mods)

	print("\n")
	print(vals)
	print(mods)
	#x = Loader()

def valCount(lst):
	res = {}
	for i in range(len(lst)):
		if i+1 not in lst:
			res[i+1]=0
		try:
			res[lst[i]] += 1
		except KeyError:
			res[lst[i]] = 1
	#del res[0]

	return res

class Loader:
	def __init__(self):
		self.patrons = pd.read_csv("data/Responses_Test.csv")
		self.patrons["Name"] = self.patrons["Name"].map(lambda x: x.lstrip(" ").rstrip(" "))
		self.ids = {
			"Thursday, September 6: Choices [Norah Gaughan: Make It Your Own: Patterned Yoke]" : "1THU",
			"Thursday, September 6: Choices [Patty Lyons: Secret of Gauge]": "2THU",
			"Thursday, September 6: Choices [Kate Atherley: Two Socks at Once: Magic Loop]": "3THU",
			"Thursday, September 6: Choices [Julia Farwell Clay: Elizabeth Zimmerman's Percentage System]": "4THU",
			"Thursday, September 6: Choices [Beatrice Perron Dahlen: Introduction to Cables]": "5THU",
			"Thursday, September 6: Choices [Susan Mills: Sew your Own Project Bag]": "6THU",
			#"Thursday, September 6: Choices [Norah Gaughan: Make It Your Own: Patterned Yoke] DUPE":"7THU",
			#"Thursday, September 6: Choices [Patty Lyons: Secret of Gauge] DUPE":"8THU",
			#"Thursday, September 6: Choices [Kate Atherley: Two Socks at Once: Magic Loop] DUPE": "9THU",
			#"Thursday, September 6: Choices [Julia Farwell Clay: Elizabeth Zimmerman's Percentage System] DUPE": "10THU",
			#"Thursday, September 6: Choices [Beatrice Perron Dahlen: Introduction to Cables] DUPE":"11THU",
			#"Thursday, September 6: Choices [Susan Mills: Sew your Own Project Bag] DUPE": "12THU",
			"Friday morning, September 7 [Julia Farwell Clay: Steeks!]": "1FRIM",
			"Friday morning, September 7 [Susan Mills: Stranded Knitting: Hat or Cowl]": "2FRIM",
			"Friday morning, September 7 [Beatrice Perron Dahlen: Shawl Shapes and Design (full day, part 1)]": "3FRIM",
			"Friday morning, September 7 [Kate Atherley: Elizabeth Zimmerman's Pi Shawl (full day, part 1)]": "4FRIM",
			"Friday morning, September 7 [Patty Lyons: Fundamentals of Sweater Design (full day part 1)]": "5FRIM",
			"Friday afternoon, September 7 [Norah Gaughan: Twisted Stitches]": "6FRIA",
			"Friday afternoon, September 7 [Susan Mills: Mitten Construction]": "7FRIA",
			"Friday afternoon, September 7 [Julia Farwell Clay: Introduction to the Prada Shell]":"8FRIA",
			"Friday afternoon, September 7 [Beatrice Perron Dahlen: Shawl Shapes part 2]": "9FRIA",
			"Friday afternoon, September 7 [Kate Atherley: Pi Shawl part 2]": "10FRIA",
			"Friday afternoon, September 7 [Patty Lyons: Fundamentals part 2]": "11FRIA",
			#"Friday morning, September 7 [Julia Farwell Clay: Steeks!] DUPE": "12FRI",
			#"Friday morning, September 7 [Susan Mills: Stranded Knitting: Hat or Cowl] DUPE":"13FRI",
			"Saturday morning, September 8 [Patty Lyons: Build a Better Fabric]": "1SATM",
			"Saturday morning, September 8 [Katharine Cobey: Basics and Beyond]": "2SATM",
			"Saturday morning, September 8 [Kristen Tendyke: Pineapple Crochet Wrap]": "3SATM",
			"Saturday morning, September 8 [Kate Atherley: Pattern Writing]": "4SATM",
			"Saturday morning, September 8 [Beatrice Perron Dahlen: Intro to Embroidery]": "5SATM",
			"Saturday morning, September 8 [Julia Farwell Clay: Decoding the Cowichan Sweater (full day part 1)]": "6SATM",
			"Saturday afternoon, September 8 [Norah Gaughan: Free Expression Cables]": "7SATA",
			"Saturday afternoon, September 8 [Beatrice Perron Dahlen: All About Lopapeyseur]": "8SATA",
			"Saturday afternoon, September 8 [Katharine Cobey: Intro to Diagonal Knitting]":"9SATA",
			"Saturday afternoon, September 8 [Kristen Tendyke: Seamless Knitted Pockets]": "10SATA",
			"Saturday afternoon, September 8 [Kate Atherley: Intro to Technical Editing]": "11SATA",
			"Saturday afternoon, September 8 [Patty Lyons: Slip Stitch & Mosaic Knitting]": "12SATA",
			"Saturday afternoon, September 8 [Julia Farwell-Clay: Decoding the Cowichan Sweater (part 2)]": "13SATA",
			"Sunday morning, September 9 [Julia Farwell-Clay: Fair Isle Mitts]": "1SUNM",
			"Sunday morning, September 9 [Kate Atherley: Intro to Brioche]": "2SUNM",
			"Sunday morning, September 9 [Norah Gaughan: Knitting With Linen]":"3SUNM",
			"Sunday morning, September 9 [Patty Lyons: Fanstastic Cast-Ons and Bind-Offs]":"4SUNM",
			"Sunday morning, September 9 [Susan Mills: Sew Your Own Needlecase]":"5SUNM"
		}
		self.daySplit = {
			#"person" :[0,3],
			"THUA" : [3, 9],
			"FRIM": [9, 14],
			"FRIA":[14, 20],
			"SATM":[20,26],
			"SATA":[26, 33],
			"SUNM": [33, 38]
		}
		self.patrons = self.cleanData(self.patrons)
		self.splitFrameByDays(self.patrons)
		self.ridDuplicates(self.datasets)
		pass

	def idClasses(self, df):
		#TODO id the classes in the dataset
		pass

	def splitFrameByDays(self, df):
		self.datasets = {}
		for key in self.daySplit:
			self.datasets[key] = df.iloc[:, self.daySplit[key][0]:self.daySplit[key][1]]
		#TODO split by days
		pass

	def cleanData(self, df):
		#TODO make sure sorted by timestamp
		frame = df.copy()
		frame.rename(columns=self.ids, inplace = True) #Renaming classname columns with ids for simplicity
		for index, row in frame.iterrows():
			if len(row) != len(set(row)):
				pass
			pass
		return frame
		#TODO make dataset not have duplicate class requests
		#TODO cleanData in general
		pass

	def ridDuplicates(self, datasets):
		for dataset in datasets:
			print("----------------NEW DATASETS-----------------")
			for index, row in datasets[dataset].iterrows():
				print(datasets[dataset].iloc[index])
				if len(datasets[dataset].iloc[index]) != len(set(datasets[dataset].iloc[index])):
					print("\t --DUPE")
				vc = valCount(row)
				print(vc)
				#for i, val in vc.items():
				#	print(i, ", ", val)
	def sort_clients(self, frame):
		#TODO sort patrons
		self.patrons_final = self.patrons.copy()
		pass

if __name__ == "__main__":
	main()
