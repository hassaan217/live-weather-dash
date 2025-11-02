# Components

This document outlines the component architecture, categories, and conventions.

### Component Architecture (proposed structure)

src/
├── components/                # Reusable UI Components
│   ├── Weather/               # Weather-specific components
│   │   ├── CurrentWeatherCard.jsx
│   │   ├── ForecastChart.jsx
│   │   └── WeatherMap.jsx
│   ├── Charts/                # Chart components
│   │   ├── LineChart.jsx
│   │   ├── BarChart.jsx
│   │   └── ComposedChart.jsx
│   ├── UI/                    # General UI components
│   │   ├── SearchBar.jsx
│   │   ├── LoadingSkeleton.jsx
│   │   └── ErrorBoundary.jsx
│   └── Layout/                # Layout components
│       ├── Header.jsx
│       ├── Footer.jsx
│       └── Sidebar.jsx
├── context/                   # React Context for State Management
│   ├── WeatherContext.jsx
│   └── ThemeContext.jsx
├─��� hooks/                     # Custom React Hooks
│   ├── useWeatherData.js
│   └── useTheme.js
├── services/                  # API Services
│   ├── weatherService.js
│   └── mapService.js
├── utils/                     # Utility Functions
│   ├── dateUtils.js
│   ├── weatherUtils.js
│   └── mapUtils.js
├── styles/                    # Global Styles
│   ├── globals.css
│   └── themes.css
└── types/                     # TypeScript Type Definitions
    ├── weather.d.ts
    └── api.d.ts

### Key Components in current codebase
- SearchBar.jsx: location search input with debounced querying and recent selections.
- CurrentWeatherCard.jsx: displays current temperature, conditions, and key stats.
- ForecastChart.jsx: multi-day forecast chart.
- HourlyChart.jsx: hourly breakdown chart.
- WindHumidityChart.jsx: wind and humidity visualization.
- WeatherMap.jsx: interactive map with weather overlays.
- AnalyticsCards.jsx: KPI cards highlighting insights and anomalies.
- KPICards.jsx: additional KPI summaries.
- RiskAlertsPanel.jsx: weather risk alert banners/panels.
- ClimateComparisonPanel.jsx: compare climates across searched locations.
- RecentSearches.jsx: list of recent locations with quick re-query.
- DataExportButton.jsx: export current view data to CSV/JSON.
- ErrorBoundary.jsx: catches runtime errors in the subtree.
- AnimatedBackground.jsx: dynamic background that reflects conditions/theme.
- Footer.jsx, LoadingSkeleton.jsx, WeatherInsights.jsx: auxiliary UI.

Conventions:
- Components are functional and use hooks.
- Styling via Tailwind utility classes.
- Props are kept minimal; shared state via context.
