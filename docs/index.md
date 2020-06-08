---
title: About the Project
keywords: homepage
sidebar: home_sidebar
permalink: index.html
---

## Abstract
Current goal of the project involves tracking a person's face and obscuring it with a 2D or 3D image, and based on a specific 'L' word spoken, like love, loathe, loss, etc., the image changes to a representation of the word.

## Draft Concept Diagram
{{site.data.mermaid.start}}
graph TD

  a[Facial Detection]
  b[Facial Tracking]
  c[Facial Morph/Distortion]
  d[Capture Sound]
  e[Train/PreTrained Network]
  f[Deep/Transfer Learning]
  w[Neural Style Transfer]
  

 subgraph Image Processing
    a --> c
    a --> b    

    c --> w
  end

  subgraph Speech Processing / NLPish
    d --> e
    e --> f
    f --> c        
  end
{{site.data.mermaid.end}}