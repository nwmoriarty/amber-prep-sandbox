import os, sys

error_strings = [
  'IndexError: list index out of range',
  'Check contents of "leap.log"',
  'ValueError: invalid literal for int() with base 16:',
  'of bcc() in charge.c properly, exit',
  'assert (ero.return_code == 0)',
  'in judgebondtype() of antechamber.c properly, exit',
  'assert 0',
  '''raise IOError('%s does not exist' % filename)''',
  'Sorry: Error interpreting command line argument as parameter definition:',
  ]

last_lines = [
  'os.system(cmd)',
  'Already done',
  ]

def run():
  results = {}
  for filename in sorted(os.listdir('output')):
    lines = open(os.path.join('output',filename), 'rb').readlines()
    pdb_code=None
    for line in lines:
      print line
      if line.find('... ')==0:
        pdb_code = line.split()[-1]
        results.setdefault(pdb_code, None)
      if line.find('Running phenix.refine')>-1:
        results[pdb_code]='Running phenix.refine'
      for es in error_strings:
        if line.find(es)>-1:
          results[pdb_code]=es
          break
      if pdb_code and results[pdb_code]: break

    assert pdb_code
    print pdb_code, filename, line
    for ll in last_lines:
      if line.find(ll)>-1:
        results[pdb_code] = 'not finished'
    assert results[pdb_code]

  nums = {}
  for pdb_code, error in results.items():
    nums.setdefault(error, [])
    nums[error].append(pdb_code)
  for error, pdb_codes in nums.items():
    print '%-60s %3d %s' % (error, len(pdb_codes), pdb_codes[:10])
    
if __name__=="__main__":
  run()#sys.argv[1])
  
