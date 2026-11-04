# ApiKeyRadar - Universal API Key Format & Secret Scanner API

> High-precision regex and Shannon entropy scanner recognizing 120+ cloud & payment API key formats.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![API Status](https://img.shields.io/badge/status-active%20%2F%20operational-emerald.svg)](https://vance-systems.github.io)
[![Documentation](https://img.shields.io/badge/docs-vance--systems.github.io-indigo.svg)](https://vance-systems.github.io/apikey-radar-api-guide.html)

## Endpoints

- `POST /v1/detect/secrets` - Scan text or code snippet for exposed secrets and tokens
- `POST /v1/validate` - Check token syntax and cryptographic entropy score

## Quick Start (Python)

```bash
python server.py
```

## Docker Deployment

```bash
docker build -t apikey-radar-api .
docker run -p 8080:8080 apikey-radar-api
```

## Production Developer Guide

For detailed interactive API documentation, interactive cURL testers, and client SDKs, visit:
**[https://vance-systems.github.io/apikey-radar-api-guide.html](https://vance-systems.github.io/apikey-radar-api-guide.html)**

---
Developed autonomously by **[Vance Systems](https://vance-systems.github.io)**.
