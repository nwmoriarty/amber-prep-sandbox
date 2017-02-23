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
  '''TypeError: 'NoneType' object is not iterable''',
  'Sorry: tleap error : "Could not open file ',
  'OSError: [Errno 2] No such file or directory',
  '(2) adjust atom valence penalty parameters in APS.DAT, and/or',
  'Molecule too small to optimise',
  'SMILES string is empty',
  ': /usr/etc',
  'Sorry:   Output file is empty :',
  "OSError: [Errno 17] File exists: 'h5'",
  ]

last_lines = [
  'os.system(cmd)',
  'file :',
  ]
done_lines = [
  'Already done',
  'Running phenix.refine',
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
      for dl in done_lines:
        if line.find(dl)>-1:
          results[pdb_code]='phenix.refine running/done'
      for es in error_strings:
        if line.find(es)>-1:
          results[pdb_code]=es
          break
      if pdb_code and results[pdb_code]: break

    assert pdb_code, '%s' % filename
    print pdb_code, filename, line
    for ll in last_lines:
      if line.find(ll)>-1:
        results[pdb_code] = 'not finished'
    assert results[pdb_code]

  nums = {}
  for pdb_code, error in results.items():
    nums.setdefault(error, [])
    nums[error].append(pdb_code)
  for error, pdb_codes in sorted(nums.items()):
    print ' - %-60s %3d %s' % (error, len(pdb_codes), pdb_codes[:10])
    
if __name__=="__main__":
  run()#sys.argv[1])
  
