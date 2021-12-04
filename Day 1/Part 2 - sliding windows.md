# Input

		input ← 199 200 208 210 200 207 240 269 260 263
		
	199 200 208 210 200 207 240 269 260 263
	
# Sliding Window Folds

## Add all the input values

		+/ input

	2256

## Pairwise Addition Fold

		2+/ input

	399 408 418 410 407 447 509 529 523

## Sliding 3-value Window Addition Fold

		3+/ input

	607 618 618 617 647 716 769 792
	
# Combining operators

## Pairwise-Increasing Windows

		2</3+/ input
	
	1 0 0 1 1 1 1
	
## Count Pairwise-Increasing Windows
		+/2</3+/ input
	
	5
	
# Final Program
	+/2</3+/ input
	
# Answer
	5
