Yet another flatter!!. Python Handler to flatten a deep-nested JSON 
Features:
Proper handler for deep-nested objects. It was initially created to handle cases with eleven nested levels. 
Generate names, or FQN (full qualified name), for the dicts and lists for input entries without names. Name for every value. 
Smooth integration with consumer applications This flatter produces a configurable irritable list for further processing.
Visualized chain string to show the naming hierarchy for each value. 
Configuration: 
The file name is ""scan_capture.ini"" and is located in the "base.cfg.INI" folder.
Naming:
The FQN shows the hierarchy names for each value.
The generated names are not interfering with the existing names in the input object. The fixed-length format and source identifier are in place. 
to distinguish generated names from the input names. Fixed Length is used to avoid any separator that may be part of any real name object. 
Three types of FQN are provided: tokens, composed names, and chain descriptive names. The title given for the chain of descriptive names is "Visual Interpretation.".
Token and Composed are used for applications integrated with the flatter. Chain descriptive names are visualized in the hierarchy for the QFN, which helps decision-makers.
The DB, Dict-like structure, and annotation are typical use cases for these FQNs. 
For the same json-object type and the positional hierarchy, the generated names are the same. Consistence, or the same name for the same object type, is crustal for periodic loading. 
Accumulated data from periodic loading with consistency minimizes the misleadingness of weighted value analyses. 
To keep this feature functioning properly across multiple periodical runs, the CFG value for the "generator" section in the CFG file should be the same.

Run Modes:
File Mode: produce a file with the above 3 columns along with their associated values. The CFG file needs three parameters for this mode.
The parameters are: inp_json_file, out_file_results, and "list2Application=False. "Executing "scan_capture.py" will produce the output file.
Integration Mode: output from flatter will be further consumed by other applications.
There is a need to receive the FQNs and values list for further processing. The CFG file needs three parameters for this mode.
The parameters are inp_json_file and "list2Application=True.".
The template "out_list_2_application.py" shows how to integrate or wire the flatter with any Python application.
