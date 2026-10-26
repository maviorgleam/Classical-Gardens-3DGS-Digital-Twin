# Classical-Gardens-3DGS-Digital-Twin
Lightweight Reconstruction of Classical Gardens Based on 3D Gaussian Splatting

## About This Project
This is a supporting research project exploring the application and lightweight optimization of 3D Gaussian Splatting (3DGS) in large-scale outdoor cultural heritage scenarios, using the Liuhe Pagoda Garden as a case study.

## Project Background
Traditional mesh-based photogrammetry struggles to accurately represent soft details such as vegetation and translucent materials in classical gardens, and the heavy model size makes it difficult to support lightweight metaverse roaming. The standardized optimization workflow and quantitative assessment framework of 3DGS in the cultural heritage field still lack empirical validation.

## My Role & Contributions
**Role**: Core Research Team Member

**Contributions**：
I was responsible for multi-perspective image acquisition, lightweight optimization scheme design, and full-dimensional quantitative performance testing for the project.

### 1. Dataset Construction & Preprocessing
Collected over 500 multi-view images covering architectural features, pathways and vegetation of the classical garden scene.
Completed dataset standardization and preprocessing to support baseline 3DGS model training.

### 2. Lightweight Optimization Scheme Design
Designed an interactive denoising and lightweight optimization solution based on the SuperSplat tool.
Removed floating artifacts and redundant background points through ROI cropping and manual refinement, achieving 25.5% reduction in Gaussian points while maintaining over 90% visual fidelity.

### 3. Three-Dimensional Quantitative Evaluation
Established a three-dimensional evaluation framework covering visual fidelity, model volume and real-time frame rate.
Completed comparative tests across multiple hardware configurations, verifying stable 60 FPS operation on mid-to-high-end GPUs and 35–42 FPS on integrated graphics.

## Technical Implementation
- **Core Technology**: 3D Gaussian Splatting (based on open-source framework)
- **Optimization Tool**: SuperSplat interactive editor
- **Evaluation Metrics**: Gaussian point count, model size, rendering FPS, visual fidelity

## Repository Structure
This repository includes the modules I was personally responsible for:
- **scripts** – Python scripts for dataset preprocessing, optimization effect statistics and 3D performance evaluation
- **configs** – Parameter configuration files for SuperSplat lightweight optimization
- **results** – Summary of core test metrics and comparative analysis results

## Supplementary Materials
- Full research process, optimization workflow and quantitative test results are presented in detail in the portfolio and project report.
- Core findings provide technical and methodological support for the metaverse deployment of cultural heritage spatial scenes.

## Notes
- This is a collaborative team course project. I was primarily responsible for image acquisition, optimization design and performance evaluation; 3DGS baseline model training was completed by other team members.
- The project is built upon the open-source 3D Gaussian Splatting framework; this repository only includes the application-side processing and evaluation work I participated in.
