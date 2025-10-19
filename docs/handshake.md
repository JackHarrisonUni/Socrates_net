# Horai Zero-Trust handshake specification

### 1 purpose
This document defines how modules must register and authenticate with the Horai module before they are trusted. Horai runs in strick Zero-trust with no module trusted by default for security purposes.

### 2 Pre.conditions for any incoming module

a module will only be allowed ro attempt a handshake if all of the following are true:

- Module must identify itself **NAME** (e.g. Plato, Hermes, Sentinel)
- Module must delare its **ROLE/PURPOSE** (e.g. analysis, scanning, IDS)
- Module must confirm **Read-only OR Read-Write INTENT**
- Module must explicitly request **TEMPORARY or PERSISTENT SESSION TRUST**


### 3 Handshake Request sequence (Initiated by Module)

The module must send the following in its initial handshake request:

1. Module_Name
2. Module_Role
3. Intent (Read-only / Read-Write)
4. Duration (Temp / Persistent)
5. OlympusKey_Request (Module asks for Horai to give it a cyrptographic key)


### 4 Handshake specification

olympusChallenge {
    challenge_id: <unique per-session identifyer that changes after C commands or M minutes>,
    olympus_token: <cryptographically secure one-time challenge value>
}


### 5 module proof and challenge

moduleProof {
    challenge_id: <must match Horai's>
    signed_response: <HMAC or digital signiture of olympus_token using module's private key>
}

### 6 Horai's response

trustGranted {
    session_id: <non-guessable unique session ID>
    access_scope: <minimum access based on role and intent>
    expiry: <time or command count>
    horai_signiture: <horai signs this entire structure>
}

trust_denied {
    reson: <minimum information for example "InvaidProof" or "UnauthorisedIntent">
}


### 7 Post Trust session rules

session rules {
    every command **MUST** have session id and horais signed key which get changed after every accepted command

    modules **Cannot** eleveate or change intent or role mis-session
    any access request declide outside of scope is terminated and so is the trust 

    commands are logged + intergrity-hashed into Lyceum (Audit storage) Horai mat force session_expirey early if abnormal behaviour is detected 
}

Key protections:
- No stale/non-rotating tokens
- No silent role escalation
- No guessing future nonces
- No persistence without permission
- All actions auditable — no invisibility


### 8 trust revokation and KILL_SWITCH behaviour

trust_revoked {
    Trigger:
        - invalid or replayed key
        - attempt to access outside scope
        - attempt to change role/intent mid session
        - session id/signature mismatch
        -rate limit / brute force anomaly
        -abnormal timing / out of order comand patters
        - any attempt to send unsigned or plaintext command  
}

effect : 
    - imediate session termination
    - all keys invalidated
    - module blacklisted for cooldown period (perma if malicious)
    - security event written to Lyceum audit log
    - Socrates notified if severity >= critical
