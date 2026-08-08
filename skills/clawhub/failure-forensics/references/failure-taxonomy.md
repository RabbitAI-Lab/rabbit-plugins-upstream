# Failure Taxonomy

A reference for categorizing failures during Phase 1 (Triage) of the forensics workflow.

## How to Use This Taxonomy

1. Read the error message / failure signature.
2. Match it against the patterns below.
3. If multiple categories match, pick the **most specific** one. A `ModuleNotFoundError` is a *dependency* failure, not an *environment* failure, even though both relate to the system.
4. If no category fits cleanly, record it as **uncategorized** and note the novel pattern. The taxonomy grows by accretion.

---

## 1. Network Failures

**Core question:** Is the endpoint reachable *right now*, and from this environment?

### Signatures

| Pattern | Meaning |
|---|---|
| `Connection refused`, `ConnectionRefusedError` | Port open but nothing listening / rejected |
| `Connection timed out`, `ETIMEDOUT` | Packet dropped, firewall, or host unreachable |
| `Name or service not known`, `NXDOMAIN` | DNS resolution failure |
| `SSL: CERTIFICATE_VERIFY_FAILED` | TLS cert expired, self-signed, or MITM |
| `HTTP 502 Bad Gateway`, `503 Service Unavailable`, `504 Gateway Timeout` | Server-side failure |
| `curl: (7) Failed to connect`, `curl: (28) Connection timed out` | CLI-level network failure |
| `ECONNRESET`, `Connection reset by peer` | Remote end dropped the connection |

### Diagnostic Questions

- Does `curl -v <url>` or `nc -zv <host> <port>` work from the same environment?
- Is this an internal vs. external endpoint? (internal may need VPN/peering)
- Is there a proxy or corporate firewall in play?
- Did this work before? What changed? (network config, DNS, certs)

### Common Root Causes

- Service is down or not started
- Wrong port number (e.g., `:443` vs `:80`)
- DNS misconfiguration or stale cache
- Expired TLS certificate
- Firewall / security group blocking the port
- IPv6 vs IPv4 resolution mismatch

---

## 2. Permissions Failures

**Core question:** Does the credential/token/user have the needed scope for this action?

### Signatures

| Pattern | Meaning |
|---|---|
| `401 Unauthorized`, `HTTP 401` | No credentials, or credentials rejected |
| `403 Forbidden`, `HTTP 403` | Credentials valid, but lack permission |
| `Permission denied`, `EACCES`, `PermissionError` | Filesystem permission denied |
| `Access denied`, `UnauthorizedAccess` | Cloud API / IAM denial |
| `insufficient privileges`, `requires elevated permissions` | OS-level privilege denial |
| `invalid token`, `token expired`, `invalid_grant` | Auth token problem |

### Diagnostic Questions

- What user/service account is the agent running as?
- What scopes/roles does the token have? (check the token's claims, not assumptions)
- Is this a filesystem permission issue (check `ls -la`, `id`, `getfacl`)?
- Is this an API/IAM issue (check the service's permission model)?
- Did the token expire? Check issuance and expiry timestamps.

### Common Root Causes

- Token expired and wasn't refreshed
- Token has correct identity but wrong scope/role
- File owned by a different user; agent running as non-root
- sudo / privilege escalation required but not available
- IAM policy missing a specific action (e.g., `s3:GetObject` but not `s3:PutObject`)

---

## 3. Logic Failures

**Core question:** What assumption did the code make that turned out to be false?

### Signatures

| Pattern | Meaning |
|---|---|
| `AssertionError` | Explicit assertion violated |
| `TypeError`, `ValueError`, `KeyError` | Unexpected data shape or type |
| Output is wrong (no exception) | Silent logic error |
| `IndexError`, `AttributeError` | Assumed structure that doesn't exist |
| Unexpected None / null | Missing value not handled |
| Off-by-one, race condition | Classic algorithmic bugs |

### Diagnostic Questions

- What did the code *expect* the input/output to be? What was it actually?
- Is this a data-dependent failure? (works on test data, fails on real data)
- Is there an implicit assumption about ordering, types, or state?
- Did the logic work before? What input changed?

### Common Root Causes

- Assumed data shape that the real data doesn't match (e.g., missing optional field)
- Assumed a side effect completed (e.g., file written) when it hadn't
- Assumed an operation was atomic when it wasn't (race condition)
- Hardcoded value that was correct in one environment but not another
- Logic that handles the happy path but not edge cases (empty list, None, concurrent access)

---

## 4. Environment Failures

**Core question:** What does the runtime environment look like vs. what the task assumed?

### Signatures

| Pattern | Meaning |
|---|---|
| `command not found`, `No such file or directory` | Binary/tool not installed or not on PATH |
| `env: ‘FOO’: No such file or directory` | Missing required environment variable |
| Wrong version output | Binary present but wrong version |
| `uname` mismatch | Wrong OS or architecture |
| `too large section header offset` | Binary compiled for different arch |
| `/usr/bin/python3: No module named pip` | Toolchain component missing |

### Diagnostic Questions

- `which <tool>` / `command -v <tool>` — is the binary on PATH?
- `<tool> --version` — is it the expected version?
- `echo $VAR` — are required env vars set?
- `uname -a` — correct OS and architecture?
- Is this running in a container, VM, or bare metal? What's the base image?

### Common Root Causes

- Tool installed in a different environment (e.g., dev machine but not CI)
- PATH doesn't include the install directory
- Wrong Docker base image
- Missing environment variable that was set in `.bashrc` but not in the agent's shell
- Architecture mismatch (e.g., arm64 binary on x86_64)

---

## 5. Dependency Failures

**Core question:** What changed in the dependency graph?

### Signatures

| Pattern | Meaning |
|---|---|
| `ModuleNotFoundError`, `ImportError` | Python package not installed |
| `Cannot find module`, `MODULE_NOT_FOUND` | Node.js package not installed |
| `NoClassDefFoundError`, `ClassNotFoundException` | Java class not on classpath |
| `pkg: unresolved dependency`, version conflict | Conflicting version requirements |
| `ABI mismatch`, `undefined symbol` | Compiled extension built for wrong version |
| `Package 'foo' not found` | Package not available in the repo |

### Diagnostic Questions

- `pip list` / `npm ls` / `gem list` — is the package installed?
- Is there a `requirements.txt` / `package-lock.json` / `Gemfile.lock` that pins versions?
- Was a dependency recently upgraded? Check `pip list --outdated` or git diff on lock files.
- Are there conflicting version requirements from different packages?

### Common Root Causes

- Package not installed in the active virtualenv / node_modules
- Version conflict: package A needs `lib>=2.0`, package B needs `lib<2.0`
- Transitive dependency changed without updating lock file
- Package installed for Python 3.11 but running on 3.9
- Compiled C-extension built against a different version of the shared library

---

## 6. Resource Failures

**Core question:** What was the ceiling, and what hit it?

### Signatures

| Pattern | Meaning |
|---|---|
| `Out of memory`, `OOMKilled`, `MemoryError` | RAM exhausted |
| `No space left on device`, `ENOSPC` | Disk full |
| `Too many open files`, `EMFILE`, `ENFILE` | File descriptor limit |
| `429 Too Many Requests`, rate limit headers | API rate limit |
| `Quota exceeded` | Cloud quota / billing limit |
| `Cannot allocate memory` | Fork/thread allocation failure |
| `SIGKILL` (exit code 137) | Process killed (often OOM killer) |

### Diagnostic Questions

- `free -h` / `df -h` — current memory and disk state
- `ulimit -n` / `cat /proc/<pid>/limits` — file descriptor limit
- For API limits: check the `X-RateLimit-Remaining` and `X-RateLimit-Reset` headers
- Is this a spike or a steady-state exhaustion?
- Was a resource leaked? (file handles not closed, memory not freed)

### Common Root Causes

- Memory leak (growing RSS over time)
- Unbounded queue / cache without eviction
- Processing a file or dataset larger than expected
- File descriptor leak (opened connections not closed)
- Too many concurrent operations hitting an API rate limit
- Log file filling the disk
- Cloud account hit a soft quota (e.g., max instances)

---

## Edge Cases and Overlaps

### Network vs. Permissions

An HTTP 401/403 from an API *looks* like a network call but is a **permissions** failure. The network worked fine — the server responded. The issue is authorization.

**Rule:** If the server responded at all (even with an error code), the network layer succeeded. Classify by the *meaning* of the response, not the fact that a request was made.

### Environment vs. Dependency

`command not found: python3` is an **environment** failure (Python itself isn't installed). `ModuleNotFoundError: No module named 'requests'` is a **dependency** failure (Python is there, but a package isn't).

**Rule:** If the *runtime* (interpreter, package manager) is missing, it's environment. If the runtime exists but a *package* within it is missing, it's dependency.

### Logic vs. Environment

Code produces wrong output. Is the code buggy (logic) or is it running in an environment where an assumption doesn't hold (environment)?

**Rule:** If the same code produces correct output in another environment, it's likely environment. If it's wrong everywhere, it's logic. When unsure, test in a clean environment first.

### Resource vs. Network

A request times out. Is it network latency or the server being overloaded?

**Rule:** Check server-side metrics if available. A timeout under normal network conditions often indicates server-side resource exhaustion (a resource failure on the *server*, even though it manifests as a network failure on the *client*).

---

## Adding to the Taxonomy

When you encounter a failure that doesn't fit any category:

1. Document it with its signature and diagnostic questions.
2. Check if it's genuinely new or an unmapped edge case of an existing category.
3. If new, add it as a sub-category or propose a new top-level category.
4. Update this file and note the addition in the post-mortem.

The taxonomy is not exhaustive by design — it's a living document that grows with experience.
