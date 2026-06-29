**FILE INTEGRITY CHECKER**



**Overview**

A Python-based File Integrity Checker that uses the SHA-256 hashing algorithm to detect whether a file has been modified.



**Features**

\- Generate SHA-256 hash

\- Save file hashes

\- Verify file integrity

\- Detect file modifications



**Technologies Used**

\- Python

\- hashlib

\- json

\- os



**How to Run**

1\. Clone the repository.

2\. Run:

&#x20;  python integrity\_checker.py

3\. Enter the path of the file you want to check.



**Example Output**



First Run:

✅ File hash saved successfully.



Second Run:

✅ File is unchanged.



After modifying the file:

❌ Warning! The file has been modified.





