def wordle():
  import random
  print()
  print("In this game, you will have six guesses to guess a five-letter word. If a letter is correct, but in the wrong place, it is underlined. If it is correct in the right place, it will become bold. Your list of unguessed letters will appear at the start of each guess to help you make your guess. Careful though, you only get six :)")
  alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  wordindex=random.randint(1,10)
  if wordindex==1:
      word="artsy"
  elif wordindex==2:
      word="spout"
  elif wordindex==3:
      word="choir"
  elif wordindex==4:
      word="lover"
  elif wordindex==5:
      word="dirty"
  elif wordindex==6:
      word="slept"
  elif wordindex==7:
      word="sound"
  elif wordindex==8:
      word="wordy"
  elif wordindex==9:
      word="poems"
  else:
      word="wider"
  wordfound=0
  count=0

  def checkifthere():
      for letter in alpha:
          if letter == newalpha:
              return True
      return False  # Only return False after checking all elements


  while wordfound==0:
      print("Unguessed letters: ")
      print(alpha)
      a=input("Enter your guess: ")
      count=count+1
      boulder=""
      add=0
      for i in range(5): 
          if a[i] == word[i]:
              newalpha="\033[1m"+ a[i] +"\033[0m"
              boulder=boulder+newalpha
              add=add+1
              if checkifthere() == True:
                  alpha.remove(a[i])
          else:
              for m in range(1,5):
                  check=0
                  underline=False
                  if a[i]==word[m]:
                      underline=True
                      check=1
                  if underline==True:
                      newalpha="\033[4m"+ a[i] +"\033[0m"
                      boulder=boulder+newalpha
                      if checkifthere() == True:
                          alpha.remove(a[i])
                      break
              if check==0:
                  boulder=boulder+a[i]
                  newalpha=a[i]
                  if checkifthere() == True:
                      alpha.remove(a[i])
      if add==5:
          print("You win!")
          return 1
      elif count==6:
          print("Sorry, you ran out of guesses, you lose!")
          return 0
      print(boulder)

wordle()
