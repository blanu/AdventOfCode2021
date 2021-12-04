# Input

		input ← 199 200 208 210 200 207 240 269 260 263
		
	199 200 208 210 200 207 240 269 260 263

# Basic Functions and Operators

## Add

		199 + 200	

	399	

## Greater Than

		2 < 3

	1

## Basic Folds

### Add all the input values

		+/ input

	2256

### Less Than Fold

This one takes some consideration to understand.

		</ input

	0	

## Pairwise Fold

### Pairwise Addition Fold

		2+/ input

	399 408 418 410 407 447 509 529 523

### Pairwise Less Than Fold

		2\>/ input

	1 1 1 0 1 1 1 0 1

## Combining operators

### Addition Fold of Pairwise Less Than Fold of Input

		+/ 2>/ input

	7

# Final Program

	+/ 2</ input

# Answer

	7
