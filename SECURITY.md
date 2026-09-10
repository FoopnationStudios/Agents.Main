# Security Policy

Agents.Main is a governance template and should never contain credentials, private keys, production data, or other secrets.

## Reporting a vulnerability

If GitHub private vulnerability reporting is enabled for this repository, use that mechanism for vulnerabilities that would be unsafe to disclose publicly. Otherwise contact the repository owner privately through an established trusted channel. Do not post live credentials, exploit secrets, private customer data, or other sensitive material in a public issue.

## Agent/security expectations

The operational rules for AI agents are in `.ai/SECURITY_RULES.md`. The baseline rejects several unsafe repository patterns mechanically, but static checks are not a security proof. Human review and GitHub repository protections remain part of the security model.

## If a secret is committed

Treat it as compromised. Remove the exposed material from active code, rotate/revoke the credential through its provider, assess logs/history and downstream use, and follow the provider's incident guidance. Merely deleting the latest copy from the repository does not make an already exposed secret trustworthy again.
