
$(".searchForm").on("submit", function(e){
    e.preventDefault();
    let form = new FormData(e.target)
    sendData(form);
    console.log(form)

})


sendData = async function(form){

    url = "http://localhost:5000/search"
    settings = {
        method: 'POST',
        body: form

    }

    
    try{
    
    let response = await fetch (url, settings)
    let data = await response.json()

    if ('results' in data){

        let result = "<div class='row g-5'>"

        for (i in data['results']){
            result += ` <div class='col'>
        <img src=${data['results'][i]['image']['url']} class='img-thumbnail text-center'>
        <div class="fs-3 text-white text-center bg-dark">${data['results'][i]['name']}</div>
        </div>
        `

        }

        result += "</div>"

        $(".results").append($(result))


    }

        }

    catch (error){
        console.log(error)
        

    }

    
    
    
//     if (data['results']){
        
//     for (let superhero in data['results']){
//         // stats = ``
//         // for (stat in Object.keys(superhero.powerstats)){
//         //     stats += stat + ": " + superhero.powerstats[stat]
//         // } <div class="fs-5>${stats}</div>


//         let result = `<div class='row'> 
//         <img src=${superhero.image.url} class='img-fluid'>
//         <div class="fs-3">${superhero.name}</div>
        
//         </div>`
//         $(".results").append($(result))
//     }
// }

// else{
//     result= `<h3>Error: ${data.error} </h3>`
//     $(".results").append($(result))
// }


}

