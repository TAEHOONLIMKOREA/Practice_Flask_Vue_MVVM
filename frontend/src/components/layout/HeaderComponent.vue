<template>
  <header class="navbar fixed-top navbar-dark navbar-expand-lg bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">3DP DX PLATFORM</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="/InsertMetadata" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Insert Machine
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/InsertMetadata">Machine Metadata</a></li>
            <li><a class="dropdown-item" href="/InsertProperty">Machine Property</a></li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/InputMaterialInit">Insert Material</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="/InsertBS" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Insert Build
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/InsertBS">Build Strategy</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="/InsertBP">Build Process</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/test">Test</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
    <div class="navbar-nav">
      <div class="nav-item text-nowrap">
        <a class="nav-link px-3" onclick="openLoginPopup()">Sign in</a>
      </div>
    </div>
  </div>
</header>
</template>

<script>
export default {
  name: "HeaderComponent",
}
</script>