## Welcome to AmberPrep sandbox

This is a subset of the directory structure used to run Phenix-Amber refinements. Currently, it has the log files and a script to catalogue the errors.

python catalogue_errors.py

ends with

 - (2) adjust atom valence penalty parameters in APS.DAT, and/or   9 ['1pge', '3nxu', '1cx2', '2pcb', '1w0e', '3nt1', '2b4z', '1ue8', '3b4x']
 - Check contents of "leap.log"                                   3 ['3ipq', '1jkx', '1fvv']
     - 3ipq: resname is a number? 'HET    965  A 801      41'
 - IndexError: list index out of range                           15 ['2jlq', '2wn9', '2w8c', '1nsk', '1gvd', '2vc2', '2uyz', '2xbm', '2xeg', '2xb4']
     - This is probably limitation in pdb4amber (new code) in detecting gap. 
 - Molecule too small to optimise                                 2 ['1rer', '1io4']
 - OSError: [Errno 2] No such file or directory                   1 ['3ll8']
 - Running elbow/antechamber for MSE                             16 ['1fg5', '2jla', '2g3k', '2dwk', '1t6i', '1xm3', '1vjl', '2cy2', '1i6k', '2axy']
 - Sorry:   Output file is empty :                               51 ['3cfb', '1c0n', '1qf6', '3lkz', '3n9g', '3hww', '1brr', '2br7', '3fg1', '2rg3']
 - ValueError: invalid literal for int() with base 16:            2 ['2b9v', '1fnt']
 - assert (ero.return_code == 0)                                  8 ['3hsh', '3bwu', '2zhx', '3oiu', '3gj0', '1fss', '3ous', '1baw']
     - may be due to minimization step (e.g: 3hsh, 2zhx)
 - assert 0                                                       1 ['1cb6']
     - this is due to there not being a valid MTZ file for phenix.refine, AmberPrep runs fine
 - in judgebondtype() of antechamber.c properly, exit             6 ['2ayl', '2onk', '2j6e', '3od5', '3cij', '1zv8']
 - not finished                                                   3 ['2ger', '2f8x', '2izz']
     - phenix.refine seems to be failing but AmberPrep is OK. Will delve deeper. NWM
 - of bcc() in charge.c properly, exit                            7 ['2q3z', '1ihi', '3oha', '3gug', '3o41', '2r8j', '3lex']
 - phenix.refine running/done                                   237 ['3kqr', '2bky', '1ar2', '2gps', '1xni', '1a9b', '1wmk', '3f6l', '2c6q', '3g4z']

You can use the [editor on GitHub](https://github.com/nwmoriarty/amber-prep-sandbox/edit/master/README.md) to maintain and preview the content for your website in Markdown files.
