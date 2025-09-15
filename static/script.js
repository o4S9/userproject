// Master_File
  let r = document.getElementById("myFileInput").value;
  let masterfile = document.getElementById("masterFile");
  function Master_File(){
     document.getElementById("masterFile").style.display = "block";
  }

    function refreshB() {
        
    }
  window.onload = function () {
    document.getElementById("formFile").value = "";
    console.log("File input cleared on page load.");
  };

//   index-file
   const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("overlay");
    const toggle = document.getElementById("menu-toggle");

    toggle.addEventListener("click", () => {
      sidebar.classList.toggle("active");
      overlay.classList.toggle("active");
    });

    overlay.addEventListener("click", () => {
      sidebar.classList.remove("active");
      overlay.classList.remove("active");
    });