pvs-formatter
========
 converts PVS Studio analyzer log file to the human-readable form
```
Viva64-EM<#~>full<#~>177<#~>main.c<#~>error<#~>V631<#~>Consider inspecting the 'unlink' function call. Defining an absolute path to the file or directory is considered a poor style.<#~>false<#~>3<#~><#~> unlink(PIDFILE);<#~><#~>
```
to:
```
main.c:177
error <V631>: Consider inspecting the 'unlink' function call. Defining an absolute path to the file or directory is considered a poor style.
code:  unlink(PIDFILE);
```
