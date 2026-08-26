# GEOSPECTRA historical prototype — retired

> **Status: RETIRED / QUARANTINED**  
> **Scientific authority: NONE**  
> **Operational use: PROHIBITED**

This public repository is retained only for historical traceability. It is not
the current ENGEOSPECTRA OMEGA system.

The former application demonstrated simple Sentinel-2 band ratios and displayed
them with mineral or element labels. Those labels were not supported mineral
identifications. Band ratios may be exploratory proxies inside a governed,
evidence-based workflow; alone, they cannot establish mineral presence,
elemental composition, grade, contained material, economic value or an
exploration target.

The runtime is intentionally disabled. The Streamlit page now displays only a
quarantine and scientific-authority notice.

## Prohibited interpretations

Repository content, a successful deployment or a passing CI check does not
establish:

- gold, lithium, REE, niobium, gemstones or PGM presence;
- mineral identity or abundance;
- grade, tonnage, volume or contained material;
- economic value;
- Mineral Resource or Ore Reserve;
- CP/QP, JORC or NI 43-101 authority.

## Governance

The governed ENGEOSPECTRA OMEGA control plane and scientific runtime are
maintained separately. This repository must not be used as a source of current
OMEGA capability claims.

## Local verification

```bash
python -m py_compile app.py tests/test_quarantine.py
python tests/test_quarantine.py
```

## Repository administration

The repository owner should archive this repository in GitHub settings after the
quarantine pull request is merged. Archiving preserves history while making the
read-only status explicit.
