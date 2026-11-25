# Week 4 — Python Security Automation

A dependency-free Python toolkit for offline security automation over explicitly
owned local files and sample logs. It demonstrates deterministic file inventory,
SHA-256 evidence hashing, secret-pattern detection, configuration checks, and
JSON assessment reports.

## Attribution

- Author: `Y_774`
- Telegram: `@Y_774`
- Instagram: `@Y.77.4`
- GitHub: [`774Yk`](https://github.com/774Yk)
- Email: `yassenalhajere@gmail.com`

## Safety boundary

The toolkit is offline by design. It reads only the local directory supplied on
the command line, performs no network requests, and does not scan websites,
companies, accounts, or infrastructure. It contains no malware, credential
 theft, persistence, DDoS, destructive exploit, or evasion mechanism.

## Quick start

```bash
python -m unittest discover -s tests -v
python tools/security_checks.py
python -m secauto.cli sample-data
python -m secauto.cli sample-data --output report.json
```

The report contains the scope, SHA-256 file inventory, and findings. Example
findings are generated only in unit-test temporary directories, never against
external systems.

## Capabilities

- Recursive local file inventory
- SHA-256 evidence hashes
- Secret-pattern detection for common training markers
- JSON configuration validation for debug mode
- Deterministic JSON output suitable for CI artifacts
- Offline operation without third-party runtime dependencies

## Files

- `secauto/engine.py` — scanning, hashing, inventory, and report engine.
- `secauto/cli.py` — local directory command-line interface.
- `tests/` — automated behavior and detection tests.
- `docs/ARCHITECTURE.md` — data flow and trust boundaries.
- `docs/THREAT_MODEL.md` — assets, threats, and controls.
- `docs/SECURITY_ASSESSMENT.md` — assessment report.
- `.github/workflows/ci.yml` — tests, linting, and secret scanning.
- `CURRICULUM_PROGRESS.md` — curriculum status.

## Responsible disclosure and ethics

Only automate checks against files and systems you own or have explicit written
authorization to assess. Minimize data collection, protect reports, respect
privacy, and route confirmed issues to the owner through the agreed channel.
This project is intentionally limited to local educational samples.

## Portfolio descriptions

**CV bullet:** Built a dependency-free Python security-automation toolkit for
local file inventory, SHA-256 evidence hashing, secret-pattern detection,
configuration checks, deterministic JSON reports, and CI validation.

**LinkedIn:** Completed Week 4 of a cybersecurity portfolio curriculum by
building a safe offline Python security-automation toolkit with reproducible
checks, evidence hashing, local sample scanning, threat modeling, and CI guards.

## License

Educational use only; see `LICENSE`.
