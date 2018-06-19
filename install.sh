# Root directory of website
root="<root>"

# Build application
echo "[?] Building application ..."
./build.py
echo "[+] Built application."

# Copy to root
cp -r "build/." "$root"
echo "[+] Copied to root: $root."
