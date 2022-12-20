# NeoTrinkey-TestBlinker

The project's goal is to give me light indicators for long-running tests using NeoTrinkey.

## How it Works
1. Pass the test command to Neo Trinkey.
2. Run the command in a subprossess. Change the status to RUNNING with light effect #1 (e.g. static white).
3. Watch the stdout in realtime. Look for keywords and apply light effects accordingly:
  a. SUCCESS - apply light effect #2 (blinking grean / rainbow).
  b. FAILED - apply light effect #3 (blinking red).
  c. WARNING (Optional) - apply light effect #4 (static / blinking yellow)
4. Touch the NeoTrinkey to cancel the light effect.

## How to Setup and Use
1. Copy the *reaction.py* file to your computer. We'll use it to trigger all test commands.
2. Add the following command to your ~/.bashrc file.
  ```sh
  alias btest='python3 ~/Documents/coding/neo_trinkey/reaction.py $(ls /dev/tty.usbmodem*)'
  ```
  The USB serial name might be different for your device, but I found this prefix "usbmodem" common for all my three NeoPixel Trinkeys.

  If your test command is always the same, you may also add it at the end of the alias. For example:
  ```sh
  alias btest='python3 ~/Documents/coding/neo_trinkey/reaction.py $(ls /dev/tty.usbmodem*) iblaze test'
  ```

3. Run your test command (or any command that sends its status to stdout). Here we run a script that prints `SUCCESS` in 2.5 seconds and then `FAILED` in another 2.5 seconds.
  ```sh
  btest loop.sh SUCCESS FAILED
  ```
  The Trinkey should blink green in 2.5 seconds and then red in another 2.5 seconds.

4. Touch the Trinkey to reset it to idle state, before you execute your next command.