function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i * i <= n; i++) if (n % i === 0) return false;
    return true;
  }
  
  function checkPrime() {
    const p = parseInt(document.getElementById("prime").value);
    const msg = document.getElementById("primeMessage");
    if (isPrime(p)) {
      msg.innerText = `${p} is a prime number.`;
      document.getElementById("generatorSection").style.display = "block";
    } else {
      msg.innerText = `${p} is not a prime number. Enter a valid prime.`;
      document.getElementById("generatorSection").style.display = "none";
    }
  }
  
  function isPrimitiveRoot(g, p) {
    let set = new Set();
    for (let i = 1; i < p; i++) set.add(Math.pow(g, i) % p);
    return set.size === p - 1;
  }
  
  function checkGenerator() {
    const g = parseInt(document.getElementById("generator").value);
    const p = parseInt(document.getElementById("prime").value);
    const msg = document.getElementById("generatorMessage");
    if (isPrimitiveRoot(g, p)) {
      msg.innerText = `${g} is a valid generator for ${p}.`;
      document.getElementById("usersSection").style.display = "flex";
    } else {
      msg.innerText = `${g} is NOT a valid generator for ${p}. Try another.`;
      document.getElementById("usersSection").style.display = "none";
    }
  }
  
  let alicePublicKey, bobPublicKey;
  
  function computePublicKey(user) {
    const p = parseInt(document.getElementById("prime").value);
    const g = parseInt(document.getElementById("generator").value);
    const privKey = parseInt(document.getElementById(user + "Private").value);
    if (privKey >= p) return alert(`Private key must be less than ${p}`);
  
    const pubKey = Math.pow(g, privKey) % p;
    document.getElementById(user + "Public").innerText = `Public Key: ${pubKey}`;
    if (user === "alice") alicePublicKey = pubKey;
    else bobPublicKey = pubKey;
  
    if (alicePublicKey && bobPublicKey)
      document.getElementById("sharePublicKeySection").style.display = "block";
  }
  
  function sharePublicKeys() {
    document.getElementById("bobPublicOnAlice").innerText = bobPublicKey;
    document.getElementById("alicePublicOnBob").innerText = alicePublicKey;
    document.getElementById("shareKeySection").style.display = "block";
  }
  
  function computeSecretKey() {
    const p = parseInt(document.getElementById("prime").value);
    const alicePrivate = parseInt(document.getElementById("alicePrivate").value);
    const bobPrivate = parseInt(document.getElementById("bobPrivate").value);
  
    const aliceShared = Math.pow(bobPublicKey, alicePrivate) % p;
    const bobShared = Math.pow(alicePublicKey, bobPrivate) % p;
  
    document.getElementById("aliceSharedKey").innerText = aliceShared;
    document.getElementById("bobSharedKey").innerText = bobShared;
  }
  