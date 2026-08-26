# Security policy

Do not open a public issue containing credentials, tokens, private keys,
Earth Engine authentication material, precise private operational locations or
controlled dataset details.

If a secret is suspected to have been exposed:

1. revoke or rotate it immediately;
2. stop affected integrations;
3. inspect commits, logs and artifacts for the exposure window;
4. remove the value from current content;
5. treat history rewriting as a separate deliberate incident-response action;
6. record remediation without reproducing the secret.

This retired public repository must not receive credentials or regain scientific
processing capabilities.
