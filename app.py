"""Historical GEOSPECTRA prototype quarantine notice.

This application intentionally performs no scientific processing. The former
band-ratio demonstration was retired because it could be misinterpreted as
mineral identification without admissible evidence.
"""

import streamlit as st

st.set_page_config(
    page_title="GEOSPECTRA — Historical Prototype",
    page_icon="🛡️",
    layout="centered",
)

st.title("GEOSPECTRA — Historical Prototype")
st.error("This prototype is retired and does not perform mineral detection.")

st.markdown(
    """
This repository is preserved only for historical traceability.

The previous demonstration used simple Sentinel-2 band ratios. Such ratios may
support exploratory remote-sensing screening in a properly governed workflow,
but they **cannot identify or confirm** gold, lithium, rare-earth elements,
niobium, gemstones, platinum-group metals, or any other mineral or element.

No output from this repository establishes:

- mineral or elemental presence;
- grade, abundance, volume, tonnage or contained material;
- economic value or exploration target authority;
- Mineral Resource or Ore Reserve;
- CP/QP, JORC or NI 43-101 authority.

The governed ENGEOSPECTRA OMEGA baseline and scientific runtime are maintained
separately. This public historical repository must not be treated as the
current OMEGA system.
"""
)

st.info(
    "Scientific authority: NONE. Runtime processing: DISABLED. "
    "Historical traceability: PRESERVED."
)
