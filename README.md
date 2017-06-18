# cozmos
Fun scripts for Anki Cozmos

**email_security.py**

Modified the original Desktop Security Guard:
- Removed all Twitter functions
- Sends an email (G-mail only) with intruder's picture
- Cozmos will have 5 seconds to find owner before sending out Intruder's picture
- Cozmos will not turn away or act "suspicious" when first encounter Intruder
- Cozmos will not be alarmed by unknown faces within 30 seconds of seeing an owner's face
- Any faces recognized by Cozmos is an owner.  Any unknown faces are Intruders.

Configuration:
- Get Gmail account
- Enable 2-step verification (https://www.google.com/landing/2step/)
- Generate an App Password  (https://security.google.com/settings/security/apppasswords)
- Modify the script with your email and app password
- Run script and have fun
