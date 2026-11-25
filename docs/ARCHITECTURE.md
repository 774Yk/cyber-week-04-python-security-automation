# Architecture

```text
+-------------------+      local filesystem      +----------------------+
| secauto CLI       | -------------------------> | sample/owned files   |
+-------------------+                            +----------------------+
          |
          v
+-------------------+      JSON report           +----------------------+
| engine.py         | -------------------------> | findings + SHA-256    |
| rules + inventory |                            | evidence artifact     |
+-------------------+                            +----------------------+
```

The tool has no network client, no subprocess execution, no credential store,
and no remote target support. The caller supplies a local directory; the engine
reads regular files, computes hashes, applies deterministic rules, and emits a
JSON report. CI runs the same checks on the repository.
