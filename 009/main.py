def main():
  print("Welcome to the secret auction program.")
  others = True
  bids = {}
  while others:
    print("What is your name? ")
    name = input()
    print("What is your bid? $")
    bid = int(input())
    bids[name] = bid
    print("Are there any others thats going to bid? 'yes' or 'no'")
    yes_no = input()
    if yes_no.lower() == 'yes':
      print()
    else:
      name, bid = find_largest(bids)
      others = False
  print(f"The highest bidder is {name} with a bid of {bid}")\
  

def find_largest(dict):
  highest = 0
  name = ""
  for key in dict:
    if dict[key] >= highest:
      highest = dict[key]
      name = key
  return name, highest

if __name__ == "__main__":
  main()