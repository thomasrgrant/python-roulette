class RouletteArrays:
	red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
	black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
	high = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
	low = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
	odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
	even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

	#progression_1 = [0.05,0.1,0.2,0.4,0.8,1.6,3.2,6.4,12.8,25.6,51.2,102.4,204.8]
	
	# Dozens
	doz1 = [1,2,3,4,5,6,7,8,9,10,11,12]
	doz2 = [13,14,15,16,17,18,19,20,21,22,23,24]
	doz3 = [25,26,27,28,29,30,31,32,33,34,35,36]
	
	col1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
	col2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
	col3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

	# Dozens
	dozen_1 = [1,2,3,4,5,6,7,8,9,10,11,12]
	dozen_2 = [13,14,15,16,17,18,19,20,21,22,23,24]
	dozen_3 = [25,26,27,28,29,30,31,32,33,34,35,36]
	
	column_1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
	column_2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
	column_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
	
	#progression_2 = [0.05,0.05,0.1,0.1,0.2,0.2,0.4,0.4,0.8,0.8,1.6,1.6
	#,3.2,3.2,6.4,6.4,12.8,12.8,25.6,25.6,51.2,51.2,102.4,102.4,204.8,204.8]
	
	# Lines = 5:1
	line_1 = [1,2,3,4,5,6]
	line_2 = [4,5,6,7,8,9]
	line_3 = [7,8,9,10,11,12]
	line_4 = [10,11,12,13,14,15]
	line_5 = [13,14,15,16,17,18]
	line_6 = [16,17,18,19,20,21]
	line_7 = [19,20,21,22,23,24]
	line_8 = [22,23,24,25,26,27]
	line_9 = [25,26,27,28,29,30]
	line_10 = [28,29,30,31,32,33]
	line_11 = [31,32,33,34,35,36]

	lines = [
        [1, 2, 3, 4, 5, 6],
        [4, 5, 6, 7, 8, 9],
        [7, 8, 9, 10, 11, 12],
        [10, 11, 12, 13, 14, 15],
        [13, 14, 15, 16, 17, 18],
        [16, 17, 18, 19, 20, 21],
        [19, 20, 21, 22, 23, 24],
        [22, 23, 24, 25, 26, 27],
        [25, 26, 27, 28, 29, 30],
        [28, 29, 30, 31, 32, 33],
        [31, 32, 33, 34, 35, 36]
    ]
	
	progression_5 = [0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 
	0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8, 0.8, 0.8, 0.8, 0.8, 1.6, 
	1.6, 1.6, 1.6, 1.6, 3.2, 3.2, 3.2, 3.2, 3.2, 6.4, 6.4, 6.4, 6.4, 6.4, 12.8, 
	12.8, 12.8, 12.8, 12.8, 25.6, 25.6, 25.6, 25.6, 25.6, 51.2, 51.2, 51.2, 51.2, 51.2]
	
	# Corner = 8:1
	corner_1 = [1,2,4,5]
	corner_2 = [2,3,5,6]
	corner_3 = [4,5,7,8]
	corner_4 = [5,6,8,9]
	corner_5 = [7,8,10,11]
	corner_6 = [8,9,11,12]

	corner_7 = [10,11,13,14]
	corner_8 = [11,12,14,15]
	corner_9 = [13,14,16,17]
	corner_10 = [14,15,17,18]
	corner_11 = [16,17,19,20]
	corner_12 = [17,18,20,21]

	corner_13 = [19,20,22,23]
	corner_14 = [20,21,23,24]
	corner_15 = [22,23,25,26]
	corner_16 = [23,24,26,27]
	corner_17 = [25,26,28,29]
	corner_18 = [26,27,29,30]

	corner_19 = [28,29,31,32]
	corner_20 = [29,30,32,33]
	corner_21 = [31,32,34,35]
	corner_22 = [32,33,35,36]
	
	progression_8 = [
	0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 
	0.1,0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 
	0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,0.2, 
	0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 
	0.8, 0.8, 0.8, 0.8, 0.8,0.8, 0.8, 0.8, 
	1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 
	3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 
	6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 
	12.8,12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 
	25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 
	51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2
	]
	
	# street = 11:1
	street_1 = [ 1, 2, 3]
	street_2 = [ 4, 5, 6]
	street_3 = [ 7, 8, 9]
	street_4 = [10,11,12]
	street_5 = [13,14,15]
	street_6 = [16,17,18]
	street_7 = [19,20,21]
	street_8 = [22,23,24]
	street_9 = [25,26,27]
	street_10 = [28,29,30]
	street_11 = [31,32,33]
	street_12 = [34,35,36]
	
	progression_11 = [
	0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 
	0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 
	0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 
	0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 
	0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 
	1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 
	3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 
	6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 
	12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 
	25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6,
	51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2
	]
	
	# split = 17:1
	split_0_1 = [ 0, 1]
	split_0_2 = [ 0, 2]
	split_0_3 = [ 0, 3]

	split_1 = [ 1, 2]
	split_2 = [ 1, 4]
	split_3 = [ 2, 3]
	split_4 = [ 2, 5]
	split_5 = [ 3, 6]
	split_6 = [ 4, 5]
	split_7 = [ 4, 7]
	split_8 = [ 5, 6]
	split_9 = [ 5, 8]
	split_10 = [ 6, 9]
	split_11 = [ 7, 8]
	split_12 = [ 7,10]
	split_13 = [ 8, 9]
	split_14 = [ 8,11]
	split_15 = [ 9,12]
	split_16 = [10,11]
	split_17 = [10,13]
	split_18 = [11,12]
	split_19 = [11,14]
	split_20 = [12,15]
	split_21 = [13,14]	 
	split_22 = [13,16]
	split_23 = [14,15]
	split_24 = [14,17]
	split_25 = [15,18]
	split_26 = [16,17]
	split_27 = [16,19]
	split_28 = [17,18]
	split_29 = [17,20]
	split_30 = [18,21]
	split_31 = [19,20]
	split_32 = [19,22]
	split_33 = [20,21]
	split_34 = [20,23]
	split_35 = [21,24]
	split_36 = [22,23]
	split_37 = [22,25]
	split_38 = [23,24]
	split_39 = [23,26]
	split_40 = [24,27]
	split_41 = [25,26]
	split_42 = [25,28]
	split_43 = [26,27]
	split_44 = [26,29]
	split_45 = [27,30]
	split_46 = [28,29]
	split_47 = [28,31]
	split_48 = [29,30]
	split_49 = [29,32]
	split_50 = [30,31]
	split_51 = [31,32]
	split_52 = [31,34]
	split_53 = [32,33]
	split_54 = [32,35]	
	split_55 = [33,36]
	split_56 = [34,35]
	split_57 = [35,36]
	
	progression_17 = [
	0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 
	0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 
	0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 
	0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 
	0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 
	0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 
	0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 
	0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 
	0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 
	0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 
	1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 
	1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 
	3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 
	3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 
	6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 
	6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 
	12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 
	12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 12.8, 
	25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6,
	25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 
	51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2,
	51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2, 51.2,
	]
	
	single_0 = [0]
	single_1 = [1]
	single_2 = [2]
	single_3 = [3]
	single_4 = [4]
	single_5 = [5]
	single_6 = [6]
	single_7 = [7]
	single_8 = [8]
	single_9 = [9]
	single_10 = [10]
	single_11 = [11]
	single_12 = [12]
	single_13 = [13]
	single_14 = [14]
	single_15 = [15]
	single_16 = [16]
	single_17 = [17]
	single_18 = [18]
	single_19 = [19]
	single_20 = [20]
	single_21 = [21]
	single_22 = [22]
	single_23 = [23]
	single_24 = [24]
	single_25 = [25]
	single_26 = [26]
	single_27 = [27]
	single_28 = [28]
	single_29 = [29]
	single_30 = [30]
	single_31 = [31]
	single_32 = [32]
	single_33 = [33]
	single_34 = [34]
	single_35 = [35]
	single_36 = [36]
	
	 # single numbers
	progression_35 = [0.05] * 35 + [0.1] * 35 + [0.2] * 35 + [0.4] * 35 + [0.8] * 35 + [1.6] * 35 + [3.2] * 35 + [6.4] * 35 + [12.8] * 35

	# Voisins
	Voisins = [1,2,3,4,7,12,15,18,19,21,22,25,26,28,29,32,35]

	Tier = [7,8,10,11,13,16,23,24,27,30,33,36]

	Orphelins = [1,6,9,14,17,20,31,34]

	# Neighbors
	Neighbors_0 =	[0,3,26,32,15]	
	Neighbors_1 =	[1,16,33,20,14] 
	Neighbors_2 =	[2,4,21,25,17]	
	Neighbors_3 =	[3,12,35,26,0]	
	Neighbors_4 =	[4,15,19,21,2]	
	Neighbors_5 =	[5,23,10,24,16] 
	Neighbors_6 =	[6,17,34,27,13] 
	Neighbors_7 =	[7,18,29,28,12] 
	Neighbors_8 =	[8,11,30,23,10] 
	Neighbors_9 =	[9,14,31,22,18] 
	Neighbors_10 = [10,8,23,5,24]  
	Neighbors_11 = [11,13,36,30,8] 
	Neighbors_12 = [12,7,28,35,3]  
	Neighbors_13 = [13,6,27,36,11] 
	Neighbors_14 = [14,1,20,31,9]  
	Neighbors_15 = [15,0,32,19,4]  
	Neighbors_16 = [16,5,24,33,1]  
	Neighbors_17 = [17,2,25,34,6]  
	Neighbors_18 = [18,9,22,29,7]  
	Neighbors_19 = [19,32,15,4,21] 
	Neighbors_20 = [20,33,1,14,31] 
	Neighbors_21 = [21,19,4,2,25]  
	Neighbors_22 = [22,31,9,18,29] 
	Neighbors_23 = [23,30,8,10,5]  
	Neighbors_24 = [24,10,5,16,33] 
	Neighbors_25 = [25,21,2,17,34] 
	Neighbors_26 = [26,35,3,0,32]  
	Neighbors_27 = [27,34,6,13,36] 
	Neighbors_28 = [28,29,7,12,35] 
	Neighbors_29 = [29,22,18,7,28] 
	Neighbors_30 = [30,36,11,8,23] 
	Neighbors_31 = [31,20,14,9,22] 
	Neighbors_32 = [32,26,0,15,19] 
	Neighbors_33 = [33,24,16,1,20] 
	Neighbors_34 = [34,25,17,6,27] 
	Neighbors_35 = [35,28,12,3,26] 
	Neighbors_36 = [36,27,13,11,30]

	#{Finalbet}
	Finalbet_0 = [0,10,20,30] 
	Finalbet_1 = [1,11,21,31] 
	Finalbet_2 = [2,12,22,32] 
	Finalbet_3 = [3,13,23,33] 
	Finalbet_4 = [4,14,24,34] 
	Finalbet_5 = [5,15,25,35] 
	Finalbet_6 = [6,16,26,36] 
	Finalbet_7 = [7,17,27] 
	Finalbet_8 = [8,18,28] 
	Finalbet_9 = [9,19,29] 
	
	#{Even Chances Combos x2}
	R_O = [1,3,5,7, 9,12,14,16,18,19,21,23,25,27,30,32,34,36,
	1,3,5,7, 9,11,13,15,17,19,21,23,25,27,29,31,33,35] 
	Red_Odd = [1,3,5,7, 9,12,14,16,18,19,21,23,25,27,30,32,34,36,
	1,3,5,7, 9,11,13,15,17,19,21,23,25,27,29,31,33,35] 

	R_E = [1,3,5,7, 9,12,14,16,18,19,21,23,25,27,30,32,34,36,
	2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36] 
	Red_Even = [1,3,5,7, 9,12,14,16,18,19,21,23,25,27,30,32,34,36,
	2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36] 

	R_L = [1,3,5,7, 9,12,14,16,18,19,21,23,25,27,30,32,34,36,
	1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18] 
	Red_Low = [1,3,5,7, 9,12,14,16,18,19,21,23,25,27,30,32,34,36,
	1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,
	19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36] 

	R_H = [1,3,5,7, 9,12,14,16,18,19,21,23,25,27,30,32,34,36] 
	Red_High = [1,3,5,7, 9,12,14,16,18,19,21,23,25,27,30,32,34,36,
	19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36] 

	#{Combo Bets}
	#{Line Combinations x2}
	Line_1_3 =	[1,2,3,4,5,6,4,5,6,7,8,9] 
	Line_1_4 = [1,2,3,4,5,6,10,11,12,13,14,15]
	Line_1_5 =	[1,2,3,4,5,6,13,14,15,16,17,18] 
	Line_1_7 =	[1,2,3,4,5,6,19,20,21,22,23,24] 
	Line_1_9 =	[1,2,3,4,5,6,25,26,27,28,29,30] 
	Line_1_11 = [1,2,3,4,5,6,31,32,33,34,35,36] 
	Line_3_5 =	[4,5,6,7,8,9,13,14,15,16,17,18] 
	Line_3_7 =	[4,5,6,7,8,9,19,20,21,22,23,24] 
	Line_3_9 =	[4,5,6,7,8,9,25,26,27,28,29,30] 
	Line_3_11 = [4,5,6,7,8,9,31,32,33,34,35,36] 
	Line_5_7 =	[13,14,15,16,17,18,19,20,21,22,23,24] 
	Line_5_9 =	[13,14,15,16,17,18,25,26,27,28,29,30] 
	Line_5_11 = [13,14,15,16,17,18,31,32,33,34,35,36] 
	Line_7_9 =	[19,20,21,22,23,24,25,26,27,28,29,30] 
	Line_7_11 = [19,20,21,22,23,24,31,32,33,34,35,36] 
	Line_9_11 = [25,26,27,28,29,30,31,32,33,34,35,36] 

	#{streets Combinations x2}
	street_1_2 = [1,2,3,4,5,6]
	street_1_3 = [1,2,3,7,8,9]
	street_1_4 = [1,2,3,10,11,12]
	street_1_5 = [1,2,3,13,14,15]
	street_1_6 = [1,2,3,16,17,18]
	street_1_7 = [1,2,3,19,20,21]
	street_1_8 = [1,2,3,22,23,24]
	street_1_9 = [1,2,3,25,26,27]
	street_1_10 = [1,2,3,28,29,30]
	street_1_11 = [1,2,3,31,32,33]
	street_1_12 = [1,2,3,34,35,36]

	street_2_3 = [4,5,6,7,8,9]
	street_2_4 = [4,5,6,10,11,12]
	street_2_5 = [4,5,6,13,14,15]
	street_2_6 = [4,5,6,16,17,18]
	street_2_7 = [4,5,6,19,20,21]
	street_2_8 = [4,5,6,22,23,24]
	street_2_9 = [4,5,6,25,26,27]
	street_2_10 = [4,5,6,28,29,30]
	street_2_11 = [4,5,6,31,32,33]
	street_2_12 = [4,5,6,34,35,36]

	street_3_4 = [7,8,9,10,11,12]
	street_3_5 = [7,8,9,13,14,15]
	street_3_6 = [7,8,9,16,17,18]
	street_3_7 = [7,8,9,19,20,21]
	street_3_8 = [7,8,9,22,23,24]
	street_3_9 = [7,8,9,25,26,27]
	street_3_10 = [7,8,9,28,29,30]
	street_3_11 = [7,8,9,31,32,33]
	street_3_12 = [7,8,9,34,35,36]

	street_4_5 = [10,11,12,13,14,15]
	street_4_6 = [10,11,12,16,17,18]
	street_4_7 = [10,11,12,19,20,21]
	street_4_8 = [10,11,12,22,23,24]
	street_4_9 = [10,11,12,25,26,27]
	street_4_10 = [10,11,12,28,29,30]
	street_4_11 = [10,11,12,31,32,33]
	street_4_12 = [10,11,12,34,35,36]

	street_5_6 = [13,14,15,16,17,18]
	street_5_7 = [13,14,15,19,20,21]
	street_5_8 = [13,14,15,22,23,24]
	street_5_9 = [13,14,15,25,26,27]
	street_5_10 = [13,14,15,28,29,30]
	street_5_11 = [13,14,15,31,32,33]
	street_5_12 = [13,14,15,34,35,36]

	street_6_7 = [16,17,18,19,20,21]
	street_6_8 = [16,17,18,22,23,24]
	street_6_9 = [16,17,18,25,26,27]
	street_6_10 = [16,17,18,28,29,30]
	street_6_11 = [16,17,18,31,32,33]
	street_6_12 = [16,17,18,34,35,36]

	street_7_8 = [19,20,21,22,23,24]
	street_7_9 = [19,20,21,25,26,27]
	street_7_10 = [19,20,21,28,29,30]
	street_7_11 = [19,20,21,31,32,33]
	street_7_12 = [19,20,21,34,35,36]

	street_8_9 = [22,23,24,25,26,27]
	street_8_10 = [22,23,24,28,29,30]
	street_8_11 = [22,23,24,31,32,33]
	street_8_12 = [22,23,24,34,35,36]

	street_9_10 = [25,26,27,28,29,30]
	street_9_11 = [25,26,27,31,32,33]
	street_9_12 = [25,26,27,34,35,36]

	street_10_11 = [28,29,30,31,32,33]
	street_10_12 = [28,29,30,34,35,36]

	street_11_12 = [31,32,33,34,35,36]

	magic_9_1 = [1,2,3,4,5,6,7,8,9] # 5
	magic_9_2 = [4,5,6,7,8,9,10,11,12] # 8
	magic_9_3 = [7,8,9,10,11,12,13,14,15] # 11
	magic_9_4 = [10,11,12,13,14,15,16,17,18] # 14
	magic_9_5 = [13,14,15,16,17,18,19,20,21] # 17
	magic_9_6 = [16,17,18,19,20,21,22,23,24] # 20
	magic_9_7 = [19,20,21,22,23,24,25,26,27] # 23
	magic_9_8 = [22,23,24,25,26,27,28,29,30] # 26
	magic_9_9 = [25,26,27,28,29,30,31,32,33] # 29
	magic_9_10 = [28,29,30,31,32,33,34,35,36] # 32

	# Rows and colomns for the labels.
	row2 = [1,4,7,10,13,16,19,22,25,28,31,34]
	row1 = [2,5,8,11,14,17,20,23,26,29,32,35]
	row0 = [3,6,9,12,15,18,21,24,27,30,33,36]
	
	colm0 = [0]
	colm1 = [1,2,3]
	colm2 = [4,5,6]
	colm3 = [7,8,9]
	colm4 = [10,11,12]
	colm5 = [13,14,15]
	colm6 = [16,17,18]
	colm7 = [19,20,21]
	colm8 = [22,23,24]
	colm9 = [25,26,27]
	colm10 = [28,29,30]
	colm11 = [31,32,33]
	colm12 = [34,35,36]