# NeoTrinkey-TestBlinker

The project's goal is to give me light indicators for long-running tests using NeoTrinkey.

## How it works
1. Pass the test command to Neo Trinkey.
2. Run the command in a subprossess. Change the status to RUNNING with light effect #1 (e.g. static white).
3. Watch the stdout in realtime. Look for keywords and apply light effects accordingly:
  a. SUCCESS - apply light effect #2 (blinking grean / rainbow).
  b. FAILED - apply light effect #3 (blinking red).
  c. WARNING (Optional) - apply light effect #4 (static / blinking yellow)
4. Touch the NeoTrinkey to cancel the light effect.
