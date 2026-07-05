# TryHackMe Room Tools
### Fools Mate
1. **[Fools Mate](https://tryhackme.com/room/foolsmate)**
   ```json
   Fools Mate {
   "status":"Easy",
   "creator": "TryHackMe & DrGonz0"
   }
   ```
   
3. **[Fools Mate, Revenge](https://tryhackme.com/room/foolsm8v2)**
   ```bash
   Fools Mate, Revenge {
   "status":"Medium",
   "creator": "TryHackMe & DrGonz0"
   }
   ```
   

### Fools Mate: How to Run It
1. **Default Run (Sends `a1` to `a8`):**
```bash
Linux
python3 fools_mate.py 10.10.186.130
python3 fools_mate_revenge.py 10.10.186.130

Windows
py fools_mate.py 10.10.186.130
py fools_mate_revenge.py 10.10.186.130

```


2. **Custom Positions Run:**
```bash
Linux
python3 fools_mate.py 10.10.186.130 --from-pos b2 --to-pos g5
python3 fools_mate_revenge.py 10.10.186.130 --from-pos b2 --to-pos g5

Windows
py  fools_mate.py 10.10.186.130 --from-pos b2 --to-pos g5
py  fools_mate_revenge.py 10.10.186.130 --from-pos b2 --to-pos g5
```
