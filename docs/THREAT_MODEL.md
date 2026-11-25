# Threat model

## Scope and assumptions

- Input is an explicitly owned local directory or the included samples.
- Reports may contain filenames and should be treated as sensitive evidence.
- The tool is defensive automation, not a remote scanner.

## Assets and threats

| Asset | Threat | Control |
|---|---|---|
| Input files | Unauthorized collection | Local path only; operator controls scope |
| Reports | Sensitive evidence leakage | User controls output destination; no upload |
| Secrets | Accidental exposure | Pattern detection and CI secret scanning |
| Findings | False confidence | Documented rule limitations and manual review |

## Safety controls

1. No URL, socket, subprocess, or remote-execution capability exists.
2. The CLI rejects missing or non-directory roots.
3. Hashes provide integrity evidence, not confidentiality.
4. Rules emit review findings and never modify or delete input files.
5. The sample dataset contains synthetic values only.
