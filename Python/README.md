Overview
This project is a modular Azure IoT device simulator designed to generate and transmit structured telemetry data to an Azure IoT Hub. It simulates a single device producing operational metrics and sending them continuously using the Azure IoT Device SDK.

The project emphasizes clean system boundaries, dependency injection, and cloud‑native design practices. It was built to explore real‑world IoT behaviors such as continuous telemetry streaming, SDK connection semantics, and message metadata handling.

Key Features
Modular architecture with clear separation of concerns

Schema‑driven telemetry generation

Azure IoT Hub integration using the official Python SDK

Environment‑secured credentials

Configurable send intervals

Custom message properties for alert signaling

Graceful startup and shutdown handling

Architecture
The project is intentionally structured as a small system rather than a single script.

Code
.
├── main.py          # Application entry point and lifecycle management
├── config.py        # Configuration and environment validation
├── telemetry.py     # Telemetry data generation and alert logic
├── iot_client.py    # Azure IoT Hub transport abstraction
└── simulator.py     # Device simulation and orchestration logic
Module Responsibilities
main.py  
Wires together the system components, manages startup and shutdown, and handles process lifecycle events.

config.py  
Loads configuration values from environment variables and validates required settings.

telemetry.py  
Defines the telemetry schema and generates simulated device data. Alert logic is kept separate from transport concerns.

iot_client.py  
Encapsulates all Azure IoT Hub SDK interactions, including connection management and message construction.

simulator.py  
Controls the simulation loop, determines when telemetry is generated, and delegates message sending to the IoT client.

Telemetry Schema
Each telemetry message includes:

timestamp — Unix timestamp of message generation

battery_voltage — Simulated battery voltage reading

operating_hours — Simulated cumulative operating time

engine_speed — Simulated engine RPM

A custom message property (batteryVoltageAlert) is attached to each message to indicate whether the battery voltage exceeds a defined threshold.

Configuration
The simulator requires an Azure IoT Hub device connection string to be provided via an environment variable:

Code
AZURE_IOT_CONNECTION
The application will fail fast if this variable is not set.

Send intervals are configurable via SEND_INTERVAL_RANGE in config.py.

Running the Simulator
Set the required environment variable:

Code
AZURE_IOT_CONNECTION=<your device connection string>
Run the application:

Code
python main.py
The simulator will connect to Azure IoT Hub and continuously send telemetry until interrupted.

Design Notes

Transport logic is isolated to allow future enhancements such as retries, backoff, or alternate transports without modifying simulation logic.

The architecture is intentionally testable and extensible, enabling future expansion to multi‑device simulation or asynchronous operation.

Future Enhancements
Structured logging and metrics

Retry and exponential backoff handling

Multi‑device simulation support

Telemetry analysis and visualization pipeline

Async transport support

Purpose
This project was built as a learning and demonstration artifact to explore Azure IoT device behavior, SDK semantics, and system‑level design patterns in a realistic but controlled environment. I was used to working more on small scripts and wanted to get more in-depth with Azure since I work more in a lakehouse setting.

Lessons Learned

Separation of concerns simplifies debugging and evolution  
Isolating telemetry generation, transport logic, and orchestration made it easier to reason about failures, validate behavior, and extend the system without cascading changes.

Observability matters even in small systems  
Without explicit logging or metrics, a functioning distributed system can appear broken. Visibility into connection state and message flow is essential for confidence and troubleshooting.

Telemetry is a contract, not just data  
Consistent field naming and schema discipline are critical, as telemetry is often consumed by downstream systems that depend on stable contracts.

Designing for extensibility early pays off  
Structuring the simulator as composable components enables future enhancements such as retries, backoff, async operation, or multi‑device simulation without architectural rework.
