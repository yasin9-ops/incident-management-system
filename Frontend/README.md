# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.


Raw signals are stored in MongoDB as an audit log. These can be retrieved and displayed in the Incident Detail view. Due to time constraints, full UI integration is not implemented but the backend supports it.


Backpressure Handling:
The system handles high-throughput signal ingestion using asynchronous background tasks and rate limiting. This prevents the system from being overwhelmed when large volumes of signals are received.


Design Patterns Used:

1. State Pattern:
The incident lifecycle (OPEN → INVESTIGATING → RESOLVED → CLOSED) is managed using controlled state transitions.

2. Strategy Pattern:
The system is designed to allow flexible handling of different incident severities and processing logic.

Sample Data:
A sample_data.json file is included to simulate failure events such as cache failures and database outages.