<script>
    export let items;
</script>

<div class="nav-container">
    <ul>
        {#each items as item}
            <li><p>{item}</p></li>
        {/each}
    </ul>
</div>

<style>
    .nav-container{
        display: flex;
        flex-direction: row;
        width: 100%;
        background-color: var(--beige);
        color: var(--soft-gray);
        text-transform: capitalize;
    }

    .nav-container ul{
        width: 100%;
        list-style-type: none;
        display: flex;
        text-align: center;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        padding: 0.5rem;
    }

    .nav-container ul li{
        margin: 0 1rem;
        cursor: pointer;
        transition: ease .2s;
    }
    .nav-container ul li:hover{
        text-decoration: underline;
        color: var(--dark-gray);
    }
</style>