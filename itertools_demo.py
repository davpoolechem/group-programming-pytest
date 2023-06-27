import sys
import itertools

def simple_demo(am): 
  am_int_to_string = {
    0: "s",
    1: "p",
    2: "d",
    3: "f",
    4: "g",
    5: "h",
  }

  shell1_am = [] 
  shell2_am = [] 

  for iam in range(0, am+1):
    shell1_am.append(am_int_to_string[iam])
    shell2_am.append(am_int_to_string[iam])

  shell_pairs = itertools.product(shell1_am, shell2_am) 

  for shell_pair in shell_pairs:
    print(shell_pair)

def more_complex_demo(am, *, num_shells=2):
  am_int_to_string = {
    0: "s",
    1: "p",
    2: "d",
    3: "f",
    4: "g",
    5: "h",
  }

  shells = {}
  for ishell in range(0, num_shells): 
    shells[ishell + 1] = []

  for iam in range(0, am+1):
    for shell, am_list in shells.items():
      am_list.append(am_int_to_string[iam])

  #shell_nlets = itertools.product(shells[1], shells[2], shell[3])
  shell_nlets = itertools.product(*shells.values())

  for shell_nlet in shell_nlets:
    print(shell_nlet)

def real_impl():
  scf_params = {
    "SCF_TYPE": [ "PK", "DIRECT", "OUT_OF_CORE" ],
    "SCF_SUBTYPE": [ "AUTO", "INCORE", "OUT_OF_CORE" ],
    "SCREENING": [ "SCHWARZ", "DENSITY", "CSAM" ],
  }

  keyword_option_pairs = []
  for keyword, options in scf_params.items():
    keyword_option_pairs.append([ (keyword, x) for x in options ])

  for keyword_option_pair in keyword_option_pairs:
    print(keyword_option_pair)
  print()

  keyword_option_combos = itertools.product(*keyword_option_pairs)
  for i, keyword_option_combo in enumerate(keyword_option_combos):
    if i < 5:
      print(keyword_option_combo)

if __name__ == "__main__":
  max_shell_am = int(sys.argv[1])
  num_shells = int(sys.argv[2])

  #simple_demo(max_shell_am) 
  more_complex_demo(int(sys.argv[1]), num_shells=num_shells)
  #real_impl()
