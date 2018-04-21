import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import itertools
import threading
import time
import sys
import csv

def main():
	x = Loader()


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

def findIndexofNum(num, vals, topdown):
	if num > len(vals):
		raise Exception("The end of the list has been reached")
	try:
		inds = []
		for i, v in enumerate(vals):
			if v == num:
				inds.append(i)
		if len(inds)>1:
			return random.choice(inds)
		else:
			return inds[0]
	except IndexError:
		if topdown:
			return findIndexofNum(num+1, vals, topdown)
		else:
			return findIndexofNum(num-1, vals, topdown)


def cleanList(list):
	done = False
	def animate():
		for c in itertools.cycle(['|', '/', u"\u2015",'\\']):
			if done:
				break
			sys.stdout.write('\rcleaning next set ' + c)
			sys.stdout.flush()
			time.sleep(0.1)
	t = threading.Thread(target=animate)
	t.start()
	vals = list
	#print(vals)
	topdown = True
	steps = 0
	while 0 in valCount(vals).values():
		steps += 1
		valcount = valCount(vals)
		if topdown:
			for i in range(len(vals)):
				if(valcount[i+1]) == 0:
					try:
						vals[findIndexofNum(i+2, vals,topdown)] -=1
					except Exception:
						#print("setting topdown False")
						topdown = False
					break
		else:
			for i in range(len(vals)):
				j = len(vals)-(i+1)
				if(valcount[j+1]) == 0:
					try:
						vals[findIndexofNum(j, vals,topdown)] +=1
					except Exception:
						#print("setting topdown True")
						topdown = True
					break

		#print(vals)
	sys.stdout.flush()
	done = True
	return vals

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
			"person" :[0,3],
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
			if dataset == 0:
				continue
			print("----------------NEW DATASETS-----------------")
			for index, row in datasets[dataset].iterrows():
				print(datasets[dataset].iloc[index])
				print(datasets[dataset].iloc[index])
				if len(datasets[dataset].iloc[index]) != len(set(datasets[dataset].iloc[index])):
					print("\t --DUPE")
					datasets[dataset].iloc[index] = cleanList(datasets[dataset].iloc[index])
				vc = valCount(row)
				print(vc)

		#cleanResponses = open('data/cleanResponses.csv', 'w')
		join = pd.concat(datasets, axis=1)
		join.to_csv("data/cleanResponses.csv")



	def sort_clients(self, frame):
		#TODO sort patrons
		self.patrons_final = self.patrons.copy()
		pass

if __name__ == "__main__":
	main()
