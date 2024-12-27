import streamlit as st

# Configurações de layout
st.set_page_config(
    page_title="Gastronomia Thalita Chagas",
    page_icon="🍴",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo visual com CSS responsivo
st.markdown("""
    <style>
    /* Estilo para telas maiores */
    .title {
        color: #d35400;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #e67e22;
        text-align: center;
        font-size: 1.5rem;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #d35400;
        font-size: 1.8rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .item {
        font-size: 1.2rem;
        margin-bottom: 0.8rem;
    }
    .price {
        color: #e67e22;
        font-weight: bold;
    }
    .contact {
        text-align: center;
        margin-top: 2rem;
        font-size: 1.2rem;
    }

    /* Estilo responsivo para telas menores */
    @media (max-width: 768px) {
        .title {
            font-size: 1.8rem;
        }
        .subtitle {
            font-size: 1.2rem;
        }
        .section-header {
            font-size: 1.5rem;
        }
        .item {
            font-size: 1rem;
        }
        .price {
            font-size: 1rem;
        }
        .contact {
            font-size: 1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Título com a logo
col1, col2 = st.columns([1, 4])
with col1:
    st.image("logo.webp", use_container_width=True)
with col2:
    st.markdown("<div class='title'>Gastronomia Thalita Chagas</div>", unsafe_allow_html=True)

# Descrição inicial
st.markdown("Este cardápio oferece uma deliciosa variedade de opções para alegrar o seu verão, desde entradas refrescantes e leves até doces irresistíveis. Desfrute dos sabores cuidadosamente preparados pela **Gastronomia Thalita Chagas**!")

# Imagens em 2 colunas (Entradas)
st.markdown("<div class='section-header'>Imagens de Entradas</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.image("Foto_4.JPG", caption="Terrines de Tomate Seco", use_container_width=True)
with col2:
    st.image("Foto_5.JPG", caption="Terrine de Salmão e Doce de Ovos e Presunto", use_container_width=True)

# Seção: Entradas e Salgados
st.markdown("<div class='section-header'>Entradas e Salgados</div>", unsafe_allow_html=True)
salgados = [
    {"item": "Torta Fria de Atum/Frango", "preco": "R$ 25,00 (1/2 kg)"},
    {"item": "Mousse de Atum", "preco": "R$ 25,00 (1/2 kg)"},
    {"item": "Mini Quiches", "preco": "R$ 35,00 (10 unidades)"},
    {"item": "Tarteletes com Creme Cheese", "preco": "R$ 40,00 (10 unidades)"},
    {"item": "Sanduíche Prensado", "preco": "R$ 40,00 (25 unidades)"},
    {"item": "Pão de Nozes", "preco": "R$ 45,00 (20 unidades)"},
    {"item": "Sanduíche com Vitel Tonê", "preco": "R$ 30,00 (10 unidades)"},
]

for salgado in salgados:
    st.markdown(f"<div class='item'><strong>{salgado['item']}</strong> - <span class='price'>{salgado['preco']}</span></div>", unsafe_allow_html=True)

# Imagens em 2 colunas (Doces)
st.markdown("<div class='section-header'>Imagens de Doces</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.image("Foto_2.jpeg", caption="Camafeus", use_container_width=True)
with col2:
    st.image("Foto_3.jpeg", caption="Quindim", use_container_width=True)

# Seção: Doces
st.markdown("<div class='section-header'>Doces</div>", unsafe_allow_html=True)
doces = [
    {"item": "Pavlova com Frutas Vermelhas", "preco": "R$ 80,00 (grande)"},
    {"item": "Mini Pavlova", "preco": "R$ 6,00 (pequena) / R$ 10,00 (média)"},
    {"item": "Quindim", "preco": "R$ 5,00 (unidade)"},
    {"item": "Camafeu", "preco": "R$ 5,00 (unidade)"},
    {"item": "Bolotone", "preco": "Consultar no privado"},
    {"item": "Torta Olho de Sogra", "preco": "R$ 80,00/kg"},
    {"item": "Torta Mineira", "preco": "R$ 35,00 (500g)"},
    {"item": "Torta Felpuda de Travessa", "preco": "R$ 35,00 (500g)"},
    {"item": "Pudim Gelado", "preco": "R$ 60,00/kg"},
    {"item": "Sorvete de Doce de Leite", "preco": "R$ 70,00/kg"},
]

for doce in doces:
    st.markdown(f"<div class='item'><strong>{doce['item']}</strong> - <span class='price'>{doce['preco']}</span></div>", unsafe_allow_html=True)

# Contato
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <div class='contact'>
        <p><strong>Contato para pedidos:</strong> (47) 98836-1578</p>
        <p><strong>E-mail:</strong> <a href='mailto:thalitachagas2005@gmail.com'>thalitachagas2005@gmail.com</a></p>
        <p><strong>Instagram:</strong> <a href='https://instagram.com/gastronomiatalitachagasitapema' target='_blank'>@gastronomiatalitachagasitapema</a></p>
    </div>
""", unsafe_allow_html=True)
