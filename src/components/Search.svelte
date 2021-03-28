<script>
    function handleSubmit(e){
        console.log(e)
    }
</script>

<div class="search-container">
    <div>
        <h2>
            Seja qual for o tamanho de seu sonho, a 
            <img src="/realiza.svg" alt=""> 
        </h2>
    </div>
    <div>
        <div>
            <form on:submit={(e)=>handleSubmit(e)}>
                <div>
                    <aside><i class="fas fa-map-marker-alt"></i></aside>
                    <input type="text" placeholder="Partindo de">
                </div>
                <div>
                    <aside><i class="fas fa-plane"></i></aside>
                    <select name="destination" id="destination">
                        <option value="international">Internacional</option>
                        <option value="national">Nacional</option>
                        <option value="both">Nacional & Internacional</option>
                    </select>
                </div>
                <div>
                    <aside><i class="fas fa-users"></i></aside>
                    <input type="number" min="0" max="6" placeholder="Quantidade de passageiros">
                </div>
                <button type="submit">Buscar</button>
            </form>
        </div>
    </div>
</div>


<style>
    .search-container{
        background-image: url('/Image.png');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: 50%;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .search-container div{
        display: flex;
    }

    .search-container > div:last-of-type{
        height: 100%;
        width: 100%;
        padding: 2rem;
    }

    .search-container > div:last-of-type > div{
        width: 100%;
        height: 100%;
        border-left: 3px solid var(--white);
        border-bottom: 3px solid var(--white);
        border-radius: 0 16px;
        display: flex;
    }

    .search-container > div:last-of-type > div form {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: flex-end;
    }
    .search-container > div:last-of-type > div form button{
        background-color: var(--secondary-color);
        border-radius: .5rem;
        height: 2rem;
        width: 8rem;
        margin-bottom: 1rem;
        padding: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        font-weight: 700;
        color: var(--white);
    }
    .search-container > div:last-of-type > div form button:hover{
        filter: opacity(.7);
    }

    .search-container > div:last-of-type > div form div{
        margin-bottom: 1rem;
    }

    .search-container > div:last-of-type > div form div aside{
        background-color: var(--white);
        display: flex;
        align-items: center;
        justify-content: center;
        width: 3rem;
        color: var(--main-color);
    }

    .search-container > div:last-of-type > div form div select{
        height: 3rem;
        width: 18rem;
        outline: none;
        background-color: var(--white);

    }
    .search-container > div:last-of-type > div form div input{
        height: 3rem;
        width: 18rem;
        outline: none;
    }

    .search-container div h2{
        color: var(--white);
        padding: 2rem;
        font-size: 2rem;
    }

    .search-container div h2 img{
        display: inline-block;
        height: 2.5rem;
        margin-bottom: -.5rem;
    }

</style>