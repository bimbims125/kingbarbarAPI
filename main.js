const greet = (nama, language) => {
  if (language === "English") {
    console.log(`Good Morning ${nama}`)
  } else if(language=== "Japan") {
    console.log(`Ohayou Gozaimas ${nama}`)
  }
}
greet("Pram","Japan")