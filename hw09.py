'''
Steven Cen, William Vongphanith
IntroCS pd6 sec10
HW09 - Seeking Analogues in Python
2021-03-09
'''

'''
Warmup-1
'''
def sleep_in(weekday, vacation):
  if weekday == True and vacation == False:
    return False
  else:
    return True
'''
---------------------------
'''

def diff21(n):
  if n > 21:
    return (n - 21) * 2
  else:
    return (21 - n)
'''
---------------------------
'''
def parrot_trouble(talking, hour):
  if talking == True and hour < 7 or talking == True and hour > 20:
    return True
  else:
    return False
'''
---------------------------
'''
def makes10(a, b):
  if a == 10 or b == 10:
    return True
  else:
    if a + b == 10:
      return True
    else:
      return False
'''
---------------------------
'''
def near_hundred(n):
  if abs(n - 100) <= 10 or abs(n - 200) <= 10:
    return True
  else:
    return False
'''
---------------------------
'''
def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  else:
    return False
'''
---------------------------
'''
def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  else:
    return a + b
'''
---------------------------
'''
def pos_neg(a, b, negative):
  if negative == True:
    if a < 0 and b < 0:
      return True
    else:
      return False
  else:
    if a > 0 and b < 0 or a < 0 and b > 0:
      return True
    else:
      return False
'''
---------------------------
'''
def not_string(str):
  if 'not' in str:
    array = str.split(" ")
    if array[0] == 'not':
      return str
    else:
      return 'not ' + str
  else:
    return 'not ' + str
'''
---------------------------
'''
def missing_char(str, n):
  oldarray = list(str)
  oldarray[n] = ""
  return ''.join(oldarray)
'''
---------------------------
'''
def front_back(str):
  if len(str) == 1:
    return str
  else:
    return str[-1:] + str[1:-1] + str[:1]
'''
---------------------------
'''
def front3(str):
  thing = str[0:3]
  return thing * 3
'''
000000000000000000000000000000000000000000000000
'''

'''
Logic-1
'''
def cigar_party(cigars, is_weekend):
  if is_weekend == True and cigars >=40:
    return True
  else:
    if cigars >=40 and cigars <= 60:
      return True
    else: return False
'''
---------------------------
'''
def squirrel_play(temp, is_summer):
  if is_summer == True:
    if temp >= 60 and temp <= 100:
     return True
    else:
      return False
  else:
    if temp >= 60 and temp <= 90:
     return True
    else:
      return False
'''
---------------------------
'''
def date_fashion(you, date):
  if (you <= 2 or date <= 2):
    return 0
  if you >= 8 or date >= 8 and not (you <= 2 or date <= 2):
    return 2
  else:
    return 1
'''
---------------------------
'''
def sorta_sum(a, b):
  if a+b >= 10 and a+b <=19:
    return 20
  else:
    return a+b
'''
---------------------------
'''
def caught_speeding(speed, is_birthday):
  if is_birthday:
    multiplier = 5
  else:
    multiplier = 0
  if speed <= 60 + multiplier:
    return 0
  if 60 + multiplier < speed <= 80 + multiplier:
    return 1
  if speed > 81:
    return 2
'''
---------------------------
'''
def love6(a, b):
  if a == 6 or b == 6:
    return True
  else:
    if a+b == 6 or abs(a-b) == 6:
      return True
    else:
      return False
'''
---------------------------
'''
def weekday(day):
  if day >= 1 and day <= 5:
    return True
  else:
    return False

def alarm_clock(day, vacation):
  multiplier1 = 0
  if weekday(day):
    multiplier1 = 0
  else:
    multiplier1 = 1
  multiplier2 = 0
  if vacation == False:
    multiplier2 = 0
  else:
    multiplier2 = 1

  if multiplier1 == 0 and multiplier2 == 0:
    return "7:00"
  if multiplier1 != multiplier2:
    return "10:00"
  else:
    return "off"

'''
---------------------------
'''
def in1to10(n, outside_mode):
  if outside_mode == True:
    if not (1 < n < 10):
      return True
    else:
      return False
  else:
    if (1 <= n <= 10):
      return True
    else:
      return False
'''
---------------------------
'''

def near_ten(num):
  strin = list(str(num))
  if (int(strin[-1]) <= 9 and int(strin[-1]) >= 8) or (int(strin[-1]) >= 0 and int(strin[-1]) <= 2):
    return True
  else:
    return False
'''
---------------------------
'''
