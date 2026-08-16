// Configuración Maestra del Cliente
const clientConfig = {
    businessName: "NOMBRE DE TU NEGOCIO",
    whatsapp: "584149634585", // Reemplazar con el número de WhatsApp del cliente
    colors: {
        primary: "#F59E0B",   // Color principal (Ámbar por defecto)
        bgDark: "#09090b",    // Fondo principal (Negro Carbón)
        bgCard: "#18181b"     // Color de las tarjetas (Gris Oscuro)
    }
};

// Auto-inyectar los colores en el CSS
document.documentElement.style.setProperty('--primary', clientConfig.colors.primary);
document.documentElement.style.setProperty('--bg-dark', clientConfig.colors.bgDark);
document.documentElement.style.setProperty('--bg-card', clientConfig.colors.bgCard);
